# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:49
# @Author  : hyc6446
# @File    : repositories.py
# @Software: PyCharm
# @Github  : https://github.com/hyc6446
# @Desc    : 数据库操作的抽象层

from fastapi import HTTPException, status

from sqlalchemy.orm import Session
from app.db.models import User, Account


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


class AccountRepository:
    def get_accounts(self, db: Session):
        """
        获取所有账户信息
        :param db:
        :return:
        """
        accounts = db.query(Account).all()
        return accounts

    def get_account(self, db: Session, user_id: int):
        """
        根据账户id获取账户信息
        :param db:
        :param account_id:
        :return:
        """
        account = db.query(Account).filter(Account.id == user_id).first()
        return account

    def create_account(self, db: Session, account: Account):
        """
        创建账户
        :param db:
        :param account:
        :return:
        """
        db_account = Account(**account.dict())
        db.add(db_account)
        db.commit()
        db.refresh(db_account)
        return db_account

    def delete_account(self, db: Session, account_id: int):
        """
        根据账户id删除账户
        :param db:
        :param account_id:
        :return:
        """
        account = db.query(Account).filter(Account.id == account_id).first()
        if not account:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="账户不存在")
        db.delete(account)
        db.commit()
        return account


user_repository = UserRepository()
account_repository = AccountRepository()
