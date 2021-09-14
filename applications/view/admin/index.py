#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : index.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 9:55
"""

from flask import Blueprint, render_template
from flask_login import login_required, current_user  # 登录校验

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.get("/")
@login_required
def index():
    user = current_user
    return render_template("admin/index.html", user=user)


# 控制台页面
@admin_bp.get('/welcome')
@login_required
def welcome():
    return render_template('admin/console/console.html')
