# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:46
# @Author  : hyc6446
# @File    : routers.py
# @Software: PyCharm
# @Desc    :集中管理 API 路由

from fastapi import APIRouter
from app.api.endpoints import user


api_router = APIRouter()
api_router.include_router(user.router, prefix="/users", tags=["users"])
# api_router.include_router(item.router, prefix="/items", tags=["items"])