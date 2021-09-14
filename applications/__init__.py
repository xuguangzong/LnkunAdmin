#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : __init__.py.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 13:30
"""

import os
from flask import Flask
from .configs import common
from .configs.config import config
from applications.view import init_view

from applications.extensions import init_plugs
from applications.common.script import init_script


def create_app(config_name=None):
    app = Flask(__name__)
    if not config_name:
        # 尝试从本地环境中读取
        # 设置环境变量 os.environ["dddd"] = "999" 取出os.getenv("dddd", 67)
        config_name = os.getenv("FLASK_CONFIG", "development")
    # 引入数据库配置

    app.config.from_object(common)
    app.config.from_object(config[config_name])
    # 注册各种插件
    init_plugs(app)
    # 注册路由
    init_view(app)
    # 注册命令
    init_script(app)

    logo()

    return app


def logo():
    print('''
     _____                              _           _         ______ _           _    
    |  __ \                    /\      | |         (_)       |  ____| |         | |   
    | |__) |__  __ _ _ __     /  \   __| |_ __ ___  _ _ __   | |__  | | __ _ ___| | __
    |  ___/ _ \/ _` | '__|   / /\ \ / _` | '_ ` _ \| | '_ \  |  __| | |/ _` / __| |/ /
    | |  |  __/ (_| | |     / ____ \ (_| | | | | | | | | | | | |    | | (_| \__ \   < 
    |_|   \___|\__,_|_|    /_/    \_\__,_|_| |_| |_|_|_| |_| |_|    |_|\__,_|___/_|\_\\

        ''')
