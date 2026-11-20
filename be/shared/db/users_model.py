from shared.db.database import Base
from sqlalchemy import Column, DateTime, Enum, Integer, String, func

class User(Base):
    __tablename__ = "USERS"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    user_email = Column(String, nullable=False, unique=True)
    mobile_number = Column(String, nullable=True, unique=True)
    user_password = Column(String, nullable=False)
    user_role = Column(
        Enum("admin", "users", name="user_role_enum", native_enum=False, create_constraint=True),
        nullable=False,
    )
    state = Column(String, nullable=True)
    city = Column(String, nullable=True)
    pincode = Column(String, nullable=True)
    address = Column(String, nullable=True)
    user_status = Column(String, nullable=True)  # e.g., active, inactive
    user_updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )
    user_created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)