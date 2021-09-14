#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_photo.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 10:50
"""
from applications.extensions import ma
from marshmallow import fields


class PhotoSchema(ma.Schema):
    id = fields.Integer()
    name = fields.Str()
    href = fields.Str()
    mime = fields.Str()
    size = fields.Str()
    ext = fields.Str()
    create_time = fields.DateTime()
