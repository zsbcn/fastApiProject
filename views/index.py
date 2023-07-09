# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : index.py
# Time       ：2023/6/22 12:41
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""

import anyio
from fastapi import APIRouter

from load_config import global_config
from utils.logger import MyLogger

route = APIRouter(prefix="/index", tags=["Login"])

logger = MyLogger(__name__, global_config.load("log.level")).setConsole().getLogger()


@route.get("/")
async def login():
    logger.debug("测试")
    await anyio.sleep(5)
    return "请先登录"


@route.get("/logout")
async def logout():
    logger.debug("测试")
    return "已退出登录"
