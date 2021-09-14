#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : admin_log.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 14:11
"""
import datetime
from applications.extensions import db


class AdminLog(db.Model):
    __tablename__ = 'admin_admin_log'
    id = db.Column(db.Integer, primary_key=True)
    method = db.Column(db.String(10))
    uid = db.Column(db.Integer)
    url = db.Column(db.String(255))
    desc = db.Column(db.Text)
    ip = db.Column(db.String(255))
    success = db.Column(db.Integer)
    user_agent = db.Column(db.Text)
    create_time = db.Column(db.DateTime, default=datetime.datetime.now)
