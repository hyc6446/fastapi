# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:48
# @Author  : hyc6446
# @File    : models.py
# @Software: PyCharm
# @Github  : https://github.com/hyc6446
# @Desc    : 数据库模型定义

# 导入数据库相关模块
from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from app.db.database import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False, index=True)
    description = Column(String, nullable=False, index=True)

