#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_dict.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 10:50
"""
from applications.extensions import ma
from marshmallow import fields


class DictTypeSchema(ma.Schema):
    id = fields.Str(attribute="id")
    typeName = fields.Str(attribute="type_name")
    typeCode = fields.Str(attribute="type_code")
    description = fields.Str(attribute="description")
    createTime = fields.Str(attribute="create_time")
    updateName = fields.Str(attribute="update_time")
    remark = fields.Str()
    enable = fields.Str()


class DictDataSchema(ma.Schema):
    dataId = fields.Str(attribute="id")
    dataLabel = fields.Str(attribute="data_label")
    dataValue = fields.Str(attribute="data_value")
    remark = fields.Str()
    enable = fields.Str()
