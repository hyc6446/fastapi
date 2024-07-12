# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:46
# @Author  : hyc6446
# @File    : user.py
# @Software: PyCharm
# @Desc    : 处理与 users 相关的 API 端点


from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from app.db.repositories import user_repository
from app.schemas.user import UserCreate, UpdateUser, User
from app.schemas.common import Response
from app.db.database import get_db
from app.services.user_service import UserService
from typing import Annotated, List

router = APIRouter()


@router.get("/", response_model=List[User])
def get_users(db: Session = Depends(get_db)):
    users = user_repository.get_users(db)
    return users


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get a user by id.

    """
    user = user_repository.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="用户不存在")
    return user


@router.post("/", response_model=User)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.
    """
    return user_repository.create_user(db, user)


@router.get("/{user_id}/status", response_model=str)
async def get_user_status(user_id: int, db: Session = Depends(get_db)):
    """
    Get the status of a user.
    """
    user = user_repository.get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user_service = UserService(db)
    return user_service.get_user_status(user_id)
