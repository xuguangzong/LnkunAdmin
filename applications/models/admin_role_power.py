#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_role_power.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 14:12
"""
from applications.extensions import db

# 创建中间表
role_power = db.Table(
    "admin_role_power",  # 中间表名称
    db.Column("id", db.Integer, primary_key=True, autoincrement=True, comment='标识'),  # 主键
    db.Column("power_id", db.Integer, db.ForeignKey("admin_power.id"), comment='用户编号'),  # 属性 外键
    db.Column("role_id", db.Integer, db.ForeignKey("admin_role.id"), comment='角色编号'),  # 属性 外键
)
