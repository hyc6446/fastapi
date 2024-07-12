# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:48
# @Author  : hyc6446
# @File    : database.py
# @Software: PyCharm
# @Desc    :数据库引擎模块

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import setting


engine = create_engine(setting.DATABASE_URL_SQLITE, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# 数据库连接 依赖注入
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
