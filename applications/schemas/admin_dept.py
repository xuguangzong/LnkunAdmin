#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_dept.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 10:50
"""
from applications.extensions import ma
from marshmallow import fields, validate


class DeptSchema(ma.Schema):
    deptId = fields.Integer(attribute="id")
    parentId = fields.Integer(attribute="parent_id")
    deptName = fields.Str(attribute="dept_name")
    leader = fields.Str()
    phone = fields.Str()
    email = fields.Str(validate=validate.Email())
    address = fields.Str()
    status = fields.Str(validate=validate.OneOf(["0", "1"]))
    sort = fields.Integer()
