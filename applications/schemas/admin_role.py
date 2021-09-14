#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_role.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 10:51
"""
from applications.extensions import ma
from marshmallow import fields


class RoleSchema(ma.Schema):
    id = fields.Integer()
    roleName = fields.Str(attribute="name")
    roleCode = fields.Str(attribute="code")
    enable = fields.Str()
    remark = fields.Str()
    details = fields.Str()
    sort = fields.Integer()
    create_at = fields.DateTime()
    update_at = fields.DateTime()
