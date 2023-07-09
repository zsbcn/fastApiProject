# !/usr/bin/env python
# -*-coding:utf-8 -*-

"""
# File       : load_config.py
# Time       ：2023/7/9 23:24
# Author     ：zsbcn
# version    ：python 3.10
# Description：加载fastapi工程启动的配置项
"""
from functools import wraps
from typing import Optional

import yaml


def get_config_data():
    with open('config.yaml', mode='r', encoding='utf-8') as f:
        return yaml.safe_load(f)


# 装饰器函数：检查配置文件中是否配置指定参数
def check(flag: bool = False):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ret = func(*args, **kwargs)
            if flag and ret is None:
                raise KeyError(f"配置文件中未找到参数: {args[1]}")
            return ret

        return wrapper

    return inner


class Config(dict):
    """
    启动参数类，YAML中的配置项必须全为字典，不能使用列表或其他数据类型
    """

    @check()
    def load(self, keys: str) -> Optional[str]:
        temp = self
        key_list = keys.strip().split('.')
        if temp is None:
            return None
        for key in key_list:
            if key not in temp.keys():
                return None
            temp = temp[key]
        return temp


global_config: Config = Config(get_config_data())

if __name__ == '__main__':
    a = Config(get_config_data())
    print(f"原始数据：{a}")
    print(a.load("log.demo"))
