#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : routes.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 10:28
"""

from flask import jsonify
from flask import Blueprint
from flask_login import login_required
from ...common import admin

rights_bp = Blueprint("rights", __name__, url_prefix="/rights")


@rights_bp.get("/configs")
@login_required
def configs():
    return admin.get_render_config()


# 菜单
@rights_bp.get("/menu")
@login_required
def menu():
    menu_tree = admin.make_menu_tree()
    return jsonify(menu_tree)
