#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : rights.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 13:28
"""
from functools import wraps
from flask import abort, request, jsonify, session
from flask_login import login_required
from applications.common.admin_log import admin_log


def authorize(power: str, log: bool = False):
    def decorator(func):
        @login_required
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not power in session.get("permissions"):
                if log:
                    admin_log(request=request, is_access=False)
                if request.method == "GET":
                    abort(403)  # 异常处理
                else:
                    return jsonify(success=False, msg="权限不足")
            if log:
                admin_log(request=request, is_access=True)
            return func(*args, **kwargs)

        return wrapper

    return decorator
