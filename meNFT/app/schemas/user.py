# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午8:10
# @Author  : hyc6446
# @File    : user.py
# @Software: PyCharm
# @Desc    :定义 user 相关的 Pydantic 模型

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    description: str

class UserCreate(UserBase):
    pass


class UpdateUser(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True

