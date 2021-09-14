#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : validate.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 13:42
"""

# xss过滤
from flask import abort, make_response, jsonify


def xss_escape(s: str):
    if not s:
        return None
    else:
        return s.replace("&", "&amp;").replace(">", "&gt;").replace("<", "&lt;").replace("'", "&#39;").replace('"',
                                                                                                               "&#34;")


def check_data(schema, data):
    errors = schema.validate(data)
    for k, v in errors.items():
        for i in v:
            msg = "{}{}".format(k, i)
    if errors:
        abort(make_response(jsonify(result=False, msg=msg), 200))
