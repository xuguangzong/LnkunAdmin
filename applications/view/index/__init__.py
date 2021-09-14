#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : __init__.py.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 15:19
"""
from applications.view.index.index import index_bp


def register_index_views(app):
    app.register_blueprint(index_bp)
