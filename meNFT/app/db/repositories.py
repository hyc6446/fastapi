# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:49
# @Author  : hyc6446
# @File    : repositories.py
# @Software: PyCharm
# @Github  : https://github.com/hyc6446
# @Desc    : 数据库操作的抽象层

from fastapi import HTTPException,status

from sqlalchemy.orm import Session
from app.db.models import User


class UserRepository:

    def get_users(self, db: Session):
        """
        获取所有用户信息
        :param db:
        :return:
        """
        users = db.query(User).all()
        return users

    def get_user(self, db: Session, user_id: int):
        """
        根据用户id获取用户信息
        :param db:
        :param user_id:
        :return:
        """
        user = db.query(User).filter(User.id == user_id).first()
        return user

    def create_user(self, db: Session, user: User):
        """
        创建用户
        :param db:
        :param user:
        :return:
        """
        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


user_repository = UserRepository()
