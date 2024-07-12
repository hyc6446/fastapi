# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/12 下午4:32
# @Author  : hyc6446
# @File    : common.py
# @Software: PyCharm

from pydantic import BaseModel, Field
from typing import Union, List, Dict, Any, Optional


class Response(BaseModel):
    code: int = Field(..., description="响应状态码")
    message: Optional[str] = Field(None, description="响应信息")
    data: Union[None, List, Dict, Any] = Field(..., description="响应数据")
    total: Optional[int] = Field(None, description="数据总数")
