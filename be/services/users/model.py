from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from services.users.passwords import hash_password
from services.users.type import UserCreate, UserUpdate
from shared.db.users_model import User


def _commit_user(db: Session, user: User) -> User:
    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError as error:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User conflicts with an existing record or database constraint.",
        ) from error
    return user


def _get_user_or_404(db: Session, user_id: int) -> User:
    user = db.get(User, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found.",
        )
    return user


def create_user(payload: UserCreate, db: Session) -> User:
    user_data = payload.model_dump(exclude={"user_password"})
    user = User(
        **user_data,
        user_password=hash_password(payload.user_password),
    )
    return _commit_user(db, user)


def list_users(db: Session, offset: int, limit: int) -> list[User]:
    statement = select(User).order_by(User.user_id).offset(offset).limit(limit)
    return list(db.scalars(statement).all())


def get_user(user_id: int, db: Session) -> User:
    return _get_user_or_404(db, user_id)


def update_user(user_id: int, payload: UserUpdate, db: Session) -> User:
    user = _get_user_or_404(db, user_id)
    updates = payload.model_dump(exclude_unset=True)
    if not updates:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="At least one field must be provided.",
        )

    required_fields = {"user_name", "user_email", "user_password", "user_role"}
    if any(field in updates and updates[field] is None for field in required_fields):
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="Required user fields cannot be null.",
        )

    if "user_password" in updates:
        updates["user_password"] = hash_password(updates["user_password"])

    for field, value in updates.items():
        setattr(user, field, value)
    return _commit_user(db, user)


def delete_user(user_id: int, db: Session) -> int:
    user = _get_user_or_404(db, user_id)
    db.delete(user)
    db.commit()
    return user_id
