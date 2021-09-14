#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : init_error_views.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 15:16
"""
from flask import render_template


def init_error_views(app):
    @app.errorhandler(403)
    def page_not_found(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500
