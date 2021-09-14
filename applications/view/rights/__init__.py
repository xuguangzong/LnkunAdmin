#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : __init__.py.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 10:27
"""

from flask import Flask
from .routes import rights_bp


def register_rights_views(app: Flask):
    app.register_blueprint(rights_bp)
