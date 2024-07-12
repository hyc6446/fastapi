# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/11 下午5:47
# @Author  : hyc6446
# @File    : config.py
# @Software: PyCharm
# @Desc    : 应用的配置管理模块

from pydantic_settings import BaseSettings
from functools import lru_cache
import os


class Settings(BaseSettings):
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     print("_env_file", kwargs)
    ENVIRONMENT: str = "development"
    # project settings
    PROJECT_NAME: str = "meNFT"
    PROJECT_VERSION: str = '0.1.0'
    # api settings
    API_PREFIX: str = "/api/v1"
    # security settings
    SECRET_KEY: str = ""
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    # SQLLite settings
    DATABASE_URL_SQLITE: str = "sqlite:///./meNFT.db"
    # postgres settings
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "123456"
    POSTGRES_DB: str = "meNFT"
    POSTGRES_URL: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
    # mysql settings

    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "123456"
    MYSQL_DB: str = "meNFT"
    MYSQL_URL: str = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
    # redis settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_URL: str = f"redis://{REDIS_HOST}:{REDIS_PORT}"
    # mongodb settings
    MONGO_HOST: str = "localhost"
    MONGO_PORT: int = 27017
    MONGO_USER: str = "admin"
    MONGO_PASSWORD: str = "123456"
    MONGO_DB: str = "meNFT"
    MONGO_URL: str = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}"

    # # celery settings
    # CELERY_BROKER_URL: str = "redis://localhost:6379"
    # CELERY_RESULT_BACKEND: str = "redis://localhost:6379"

    # email settings
    # EMAIL_TEST_USER: str = "test@example.com"
    # EMAIL_TEST_PASSWORD: str = "test1234"
    # EMAIL_TEST_SMTP_SERVER: str = "smtp.gmail.com"
    # EMAIL_TEST_SMTP_PORT: int = 587
    # EMAIL_TEST_TLS: bool = True
    # EMAIL_TEST_SSL: bool = False
    # EMAIL_FROM_NAME: str = "meNFT"
    # EMAIL_FROM_EMAIL: str = "noreply@example.com"
    # EMAIL_SUBJECT_PREFIX: str = "[meNFT]"
    # EMAIL_TEMPLATES_DIR: str = "/app/email-templates/build"
    # EMAILS_ENABLED: bool = False

    class config:
        env_file = ".env.dev" if os.getenv("ENVIRONMENT") == "development" else ".env.prod"
        env_file_encoding = "utf-8"


# create settings object
@lru_cache()
def get_settings():
    environment = os.getenv("ENVIRONMENT")
    if environment == "production":
        return Settings(_env_file=".env.prod")
    else:
        return Settings(_env_file=".env.dev")


setting = get_settings()
