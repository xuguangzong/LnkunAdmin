#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : http.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 11:10
"""
from flask import jsonify


def success_api(msg: str = "成功"):
    """ 成功响应 默认值”成功“ """
    return jsonify(success=True, msg=msg)


def fail_api(msg: str = "失败"):
    """ 失败响应 默认值“失败” """
    return jsonify(success=False, msg=msg)


def table_api(msg: str = "", count=0, data=None, limit=10):
    """ 动态表格渲染响应 """
    res = {
        'msg': msg,
        'code': 0,
        'data': data,
        'count': count,
        'limit': limit

    }
    return jsonify(res)
