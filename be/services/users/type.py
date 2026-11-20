from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict

UserRole = Literal["admin", "users"]


class UserCreate(BaseModel):
    user_name: str
    user_email: str
    user_password: str
    user_role: UserRole = "users"
    mobile_number: str | None = None
    state: str | None = None
    city: str | None = None
    pincode: str | None = None
    address: str | None = None
    user_status: str | None = None


class UserUpdate(BaseModel):
    user_name: str | None = None
    user_email: str | None = None
    user_password: str | None = None
    user_role: UserRole | None = None
    mobile_number: str | None = None
    state: str | None = None
    city: str | None = None
    pincode: str | None = None
    address: str | None = None
    user_status: str | None = None


class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    user_name: str
    user_email: str
    mobile_number: str | None
    user_role: UserRole
    state: str | None
    city: str | None
    pincode: str | None
    address: str | None
    user_status: str | None
    user_updated_at: datetime
    user_created_at: datetime
