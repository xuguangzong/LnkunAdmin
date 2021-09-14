#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : init_mail.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 13:25
"""

from flask import Flask
from flask_mail import Mail

mail = Mail()


def init_mail(app: Flask):
    mail.init_app(app)
