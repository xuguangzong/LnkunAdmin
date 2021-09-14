#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_photo.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 14:12
"""
import datetime
from applications.extensions import db


class Photo(db.Model):
    __tablename__ = 'admin_photo'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    href = db.Column(db.String(255))
    mime = db.Column(db.CHAR(50), nullable=False)
    size = db.Column(db.CHAR(30), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)