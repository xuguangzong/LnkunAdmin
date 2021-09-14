#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : config.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 13:45
"""
import os
import logging


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev key')
    # redis配置
    REDIS_HOST = os.getenv('REDIS_HOST') or "127.0.0.1"
    REDIS_PORT = int(os.getenv('REDIS_PORT') or 6379)

    # mysql 配置
    MYSQL_USERNAME = os.getenv('MYSQL_USERNAME') or "root"
    MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD') or "lnkun123"
    MYSQL_HOST = os.getenv('MYSQL_HOST') or "localhost"
    MYSQL_PORT = int(os.getenv('MYSQL_PORT') or 3306)
    MYSQL_DATABASE = os.getenv('MYSQL_DATABASE') or "LnkunAdmin"

    UPLOADED_PHOTOS_DEST = '/static'

    # mysql 数据库的配置信息
    # 加f 表示在字符串内支持大括号内的表达式

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
    # 默认日志等级
    LOG_LEVEL = logging.WARN
    # 邮箱
    MAIL_SERVER = os.getenv('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_PORT = 465  # 25
    MAIL_USERNAME = os.getenv('MAIL_USERNAME') or '123@qq.com'
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD') or 'XXXXX'  # 生成的授权码
    # 默认发件人的邮箱,这里填写和MAIL_USERNAME一致即可
    MAIL_DEFAULT_SENDER = ('lnkun admin', os.getenv('MAIL_USERNAME') or '123@qq.com')


class TestingConfig(BaseConfig):
    """测试配置"""
    # DEBUG = True
    pass


class DevelopmentConfig(BaseConfig):
    """开发环境"""
    # Flask-SQLAlchemy将跟踪对象的修改并发出信号。 这需要额外的内存，如果不需要，可以禁用。
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 记录打印SQL语句用于调试的, 一般设置为False, 不然会在控制台输出一大堆的东西
    SQLALCHEMY_ECHO = False


class ProductionConfig(BaseConfig):
    """生产环境"""
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    # 多少秒后自动回收连接。这对MySQL是必要的，它默认移除闲置多于8小时的连接。注意如果使用了MySQL，Flask-SQLALchemy自动设定这个值为2小时。
    SQLALCHEMY_POOL_RECYCLE = 8
    LOG_LEVEL = logging.ERROR


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
