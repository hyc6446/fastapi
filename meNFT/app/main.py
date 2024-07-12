# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:36
# @Author  : hyc6446
# @File    : main.py
# @Software: PyCharm

from fastapi import FastAPI
import uvicorn
from app.api.routers import api_router
from app.core.config import setting
from app.db.models import Base
from app.db.database import engine

app = FastAPI(title=setting.PROJECT_NAME, version=setting.PROJECT_VERSION)
app.include_router(api_router, prefix=setting.API_PREFIX)


@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)
    print("start up event")


if __name__ == "__main__":
    uvicorn.run('run:app', host="127.0.0.1", port=9500, reload=True, ENVIRONMENT='development')
