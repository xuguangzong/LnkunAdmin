#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : init_template_directives.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 15:17
"""
from flask import session


def init_template_directives(app):
    @app.template_global()
    def authorize(power):
        return bool(power in session.get('permissions'))
