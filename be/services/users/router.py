from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from services.users.model import (
    create_user,
    delete_user,
    get_user,
    list_users,
    update_user,
)
from services.users.type import UserCreate, UserRead, UserUpdate
from shared.api.response import APIResponse
from shared.db.database import get_db

router = APIRouter()


@router.post(
    "/users",
    response_model=APIResponse[UserRead],
    status_code=status.HTTP_201_CREATED,
)
def create_user_route(
    payload: UserCreate,
    db: Session = Depends(get_db),
) -> APIResponse[UserRead]:
    return APIResponse[UserRead](
        data=create_user(payload, db),
        status=status.HTTP_201_CREATED,
        msg="User created successfully.",
    )


@router.get("/users", response_model=APIResponse[list[UserRead]])
def list_users_route(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=50, ge=1, le=100),
    db: Session = Depends(get_db),
) -> APIResponse[list[UserRead]]:
    return APIResponse[list[UserRead]](
        data=list_users(db, offset, limit),
        status=status.HTTP_200_OK,
        msg="Users retrieved successfully.",
    )


@router.get("/users/{user_id}", response_model=APIResponse[UserRead])
def get_user_route(
    user_id: int,
    db: Session = Depends(get_db),
) -> APIResponse[UserRead]:
    return APIResponse[UserRead](
        data=get_user(user_id, db),
        status=status.HTTP_200_OK,
        msg="User retrieved successfully.",
    )


@router.patch("/users/{user_id}", response_model=APIResponse[UserRead])
def update_user_route(
    user_id: int,
    payload: UserUpdate,
    db: Session = Depends(get_db),
) -> APIResponse[UserRead]:
    return APIResponse[UserRead](
        data=update_user(user_id, payload, db),
        status=status.HTTP_200_OK,
        msg="User updated successfully.",
    )


@router.delete("/users/{user_id}", response_model=APIResponse[dict[str, int]])
def delete_user_route(
    user_id: int,
    db: Session = Depends(get_db),
) -> APIResponse[dict[str, int]]:
    deleted_user_id = delete_user(user_id, db)
    return APIResponse[dict[str, int]](
        data={"user_id": deleted_user_id},
        status=status.HTTP_200_OK,
        msg="User deleted successfully.",
    )
