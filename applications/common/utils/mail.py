#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : mail.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 13:24
"""

from flask_mail import Message

from applications.extensions.init_mail import mail


# send_mail(subject='title', recipients=['123@qq.com'], content='body')
def send_mail(subject, recipients, content):
    try:
        message = Message(subject=subject, recipients=recipients, body=content)
        mail.send(message)
    except Exception as e:
        print('邮箱发送出错了')
        raise
