#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : init_apscheduler.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 13:54
"""
from flask import Flask
from flask_apscheduler import APScheduler

scheduler = APScheduler()


def init_scheduler(app: Flask):
    scheduler.init_app(app)
    with app.app_context():
        from applications.common.tasks import tasks
        scheduler.start()
        from applications.common.tasks import events
