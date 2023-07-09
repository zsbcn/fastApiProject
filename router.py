# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : router.py
# Time       ：2023/7/9 20:02
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""

from fastapi import APIRouter

from utils.logger import MyLogger
from views import index

logger = MyLogger(__name__).setConsole().getLogger()
all_router = APIRouter()

all_router.include_router(index.route)
logger.info("已加载所有路由")
