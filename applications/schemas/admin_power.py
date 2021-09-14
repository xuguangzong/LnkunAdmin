#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_power.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 10:51
"""
from applications.extensions import ma
from marshmallow import fields


# 权限models序列化类
class PowerSchema(ma.Schema):
    id = fields.Integer()
    title = fields.Str(attribute="name")
    type = fields.Str()
    code = fields.Str()
    href = fields.Str(attribute="url")
    openType = fields.Str(attribute="open_type")
    parent_id = fields.Integer()
    icon = fields.Str()
    sort = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    enable = fields.Integer()


class PowerSchema2(ma.Schema):  # 序列化类
    powerId = fields.Str(attribute="id")
    powerName = fields.Str(attribute="name")
    powerType = fields.Str(attribute="type")
    powerUrl = fields.Str(attribute="url")
    openType = fields.Str(attribute="open_type")
    parentId = fields.Str(attribute="parent_id")
    icon = fields.Str()
    sort = fields.Integer()
    create_time = fields.DateTime()
    update_time = fields.DateTime()
    enable = fields.Integer()
