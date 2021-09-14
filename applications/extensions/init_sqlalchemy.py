#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : init_sqlalchemy.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 14:16
"""

from flask import Flask, request
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy, BaseQuery
# flask_marshmallow是一个用来将复杂的orm对象与python原生数据类型之间相互转换的库
# 简而言之，就是实现object -> dict，objects -> list, string -> dict 和string -> list
# Flask-Marshmallow包含用于集成的有用附加功能Flask-SQLAlchemy和 marshmallow-sqlalchemy
# 要启用SQLAlchemy集成，请确保同时安装了Flask-SQLAlchemy和marshmallow-sqlalchemy
# 注意 Flask-SQLAlchemy必须实例化 Flask-Marshmallow前面
from flask_marshmallow import Marshmallow

from marshmallow.validate import URL, Email, Range, Length, Equal, Regexp, Predicate, NoneOf, OneOf, ContainsOnly

URL.default_message = '无效的链接'
Email.default_message = '无效的邮箱地址'
Range.message_min = '不能小于{min}'
Range.message_max = '不能小于{max}'
Range.message_all = '不能超过{min}和{max}这个范围'
Length.message_min = '长度不得小于{min}位'
Length.message_max = '长度不得大于{max}位'
Length.message_all = '长度不能超过{min}和{max}这个范围'
Length.message_equal = '长度必须等于{equal}位'
Equal.default_message = '必须等于{other}'
Regexp.default_message = '非法输入'
Predicate.default_message = '非法输入'
NoneOf.default_message = '非法输入'
OneOf.default_message = '无效的选择'
ContainsOnly.default_message = '一个或多个无效的选择'

fields.Field.default_error_messages = {
    "required": "缺少必要数据",
    "null": "数据不能为空",
    "validator_failed": "非法数据",
}

fields.Str.default_error_messages = {
    'invalid': "不是合法文本"
}

fields.Int.default_error_messages = {
    "invalid": "不是合法整数"
}

fields.Number.default_error_messages = {
    "invalid": "不是合法数字"
}

fields.Boolean.default_error_messages = {
    "invalid": "不是合法布尔值"
}


class Query(BaseQuery):
    """
    重写分页方法
    """

    def paginates(self):
        """
        表格分页
        page
        limit
        :return:
        """
        return self.paginate(page=request.args.get("page", type=int),
                             per_page=request.args.get("limit", type=int),
                             error_out=False)


db = SQLAlchemy(query_class=Query)
ma = Marshmallow()


def init_databases(app: Flask):
    db.init_app(app)
    ma.init_app(app)
