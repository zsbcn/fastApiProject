# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : views.py
# Time       ：2023/6/23 21:51
# Author     ：zsbcn
# version    ：python 3.10
# Description：
"""
from fastapi import APIRouter
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html

route = APIRouter()


@route.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(openapi_url="openapi.json", title="views",
                               swagger_js_url="static/swagger-ui/swagger-ui-bundle.js",
                               swagger_css_url="static/swagger-ui/swagger-ui.css", )


@route.get("/redoc", include_in_schema=False)
async def custom_redoc_html():
    return get_redoc_html(openapi_url="openapi.json", title="reDoc",
                          redoc_js_url="https://cdn.redoc.ly/redoc/latest/bundles/redoc.standalone.js",
                          with_google_fonts=False)


if __name__ == '__main__':
    print(getattr(__file__, 'route'))
