#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : init_debug_tool.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 15:14
"""
from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


def init_debug_tool(app: Flask):
    toolbar = DebugToolbarExtension()
    toolbar.init_app(app)
