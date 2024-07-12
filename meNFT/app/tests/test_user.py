# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:50
# @Author  : hyc6446
# @File    : test_user.py
# @Software: PyCharm
import pytest
from fastapi.testclient import TestClient
from app.api.endpoints.user import router

@pytest.fixture
def client():
    return TestClient(router)

def test_read_users(client):
    # 测试正常情况
    response = client.get("/")
    assert response.status_code == 200  # 检查状态码是否为200
    assert response.json() == {"users": ["user1", "user2"]}  # 检查返回的数据是否正确

def test_read_users_edge_cases(client):
    # 测试边缘情况，例如路径不存在
    response = client.get("/nonexistent")
    assert response.status_code == 404  # 检查状态码是否为404
