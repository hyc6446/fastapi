# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:49
# @Author  : hyc6446
# @File    : user_service.py
# @Software: PyCharm
# @Desc    : 用户业务逻辑层

from sqlalchemy.orm import Session


# from app.db.models import User


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_status(self, user_id: int):
        """
        获取用户状态
        :param user:
        :return:
        """
        if user_id == 1:
            return "active"
        else:
            return "inactive"
