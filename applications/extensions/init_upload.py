#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : init_upload.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 13:37
"""

from flask import Flask
from flask_uploads import configure_uploads
# IMAGES 为定义的图片文件类型，其值如下:
# IMAGES = tuple('jpg jpe jpeg png gif svg bmp'.split())
from flask_uploads import UploadSet, IMAGES

photos = UploadSet('photos', IMAGES)  # 实例化 UploadSet 对象


def init_upload(app: Flask):
    configure_uploads(app, photos)  # 将 app 的 config 配置注册到 UploadSet 实例 photos
