# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:48
# @Author  : hyc6446
# @File    : models.py
# @Software: PyCharm
# @Github  : https://github.com/hyc6446
# @Desc    : 数据库模型定义

# 导入数据库相关模块
from sqlalchemy import Column, Integer, String, TIMESTAMP, Float, Enum
from sqlalchemy.ext.declarative import declarative_base
from app.db.database import engine

Base = declarative_base()

class Gender(Enum):
    male = 1
    female = 2
    other = 3
class AccountState(Enum):
    normal = 0
    frozen = 1
    cancel = 2
    wait_audit = -1





class User(Base):
    __tablename__ = 'nft_users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False,)
    description = Column(String(255), nullable=False,)


class Account(Base):
    __tablename__ = 'nft_accounts'
    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False,)
    password = Column(String(50), nullable=False,)
    salt = Column(String(50), nullable=False,)
    gender = Column(Enum(Gender), nullable=False, default=Gender.other)
    email = Column(String(100), nullable=False,)
    phone = Column(String(20), nullable=False,)
    address = Column(String(255), nullable=False,)
    avatar = Column(String(255), nullable=False,)
    status = Column(Enum(AccountState), nullable=False, default=AccountState.wait_audit, description='0:正常，1:冻结,2:注销,-1:待审核,')
    create_time = Column(TIMESTAMP, nullable=False,)
    update_time = Column(TIMESTAMP, nullable=False,)