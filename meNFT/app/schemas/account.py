from pydantic import BaseModel, EmailStr, Field
from datetime import datetime


class AccountBase(BaseModel):
    user_name: str = Field(..., max_length=100)
    gender: int = Field(..., ge=1, le=3)
    email: EmailStr = Field(..., max_length=100)
    phone: str = Field(..., max_length=20)
    address: str = Field(..., max_length=255)
    avatar: str = Field(..., max_length=255)
    status: int = Field(..., ge=-1, le=2)
    create_time: datetime = Field(default_factory=datetime.now)
    update_time: datetime = Field(default_factory=datetime.now)


class AccountCreate(AccountBase):
    password: str = Field(..., max_length=50)


class AccountInDB(AccountBase):
    salt: str = Field(..., max_length=50)
    hashed_password: str = Field(..., max_length=50)


class Account(AccountBase):
    id: int

    class Config:
        from_attributes = True
