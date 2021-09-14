#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_log.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 10:50
"""
from applications.extensions import ma
from marshmallow import fields


class LogSchema(ma.Schema):
    id = fields.Integer()
    method = fields.Str()
    uid = fields.Str()
    url = fields.Str()
    desc = fields.Str()
    ip = fields.Str()
    user_agent = fields.Str()
    success = fields.Bool()
    create_time = fields.DateTime()
