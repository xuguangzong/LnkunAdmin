#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : curd.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 15:04
"""
from flask import Blueprint

admin_curd = Blueprint('adminCurd', __name__, url_prefix='/admin/curd')


@admin_curd.route('/')
def index():
    return "功能开发中"

