#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : __init__.py.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 15:17
"""
from applications.view.admin import register_admin_views
from applications.view.index import register_index_views
from applications.view.passport import register_passport_views
from applications.view.rights import register_rights_views
from applications.view.department import register_dept_views


def init_view(app):
    register_admin_views(app)
    register_index_views(app)
    register_rights_views(app)
    register_passport_views(app)
    register_dept_views(app)
