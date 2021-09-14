#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : index.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 9:20
"""

from flask import render_template, Blueprint

index_bp = Blueprint('Index', __name__, url_prefix="/")


@index_bp.route("/")
def index():
    return render_template('index/index.html')
