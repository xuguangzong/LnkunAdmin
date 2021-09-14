#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : initdb.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 15:31
"""
from dotenv import dotenv_values  # 环境变量加载工具
import sqlparse  # sqlparse有几个最简单的工具：split，format，parse，分别是提取sql单个语句、格式化sql的语句以及解析sql
import pymysql

config = dotenv_values('.env')
# MySql配置信息
HOST = config.get('MYSQL_HOST') or 'localhost'
PORT = config.get('MYSQL_PORT') or 3306
DATABASE = config.get('MYSQL_DATABASE') or 'LnkunAdmin'
USERNAME = config.get('MYSQL_USERNAME') or 'root'
PASSWORD = config.get('MYSQL_PASSWORD') or 'lnkun123'


def is_exist_database():
    db = pymysql.connect(host=HOST, port=int(PORT), user=USERNAME, password=PASSWORD, charset='utf8mb4')
    cursor1 = db.cursor()
    sql = "select * from information_schema.SCHEMATA WHERE SCHEMA_NAME = '%s'  ; " % DATABASE
    res = cursor1.execute(sql)
    db.close()
    return res


def init_database():
    db = pymysql.connect(host=HOST, port=int(PORT), user=USERNAME, password=PASSWORD, charset='utf8mb4')
    cursor1 = db.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS %s" % DATABASE
    res = cursor1.execute(sql)
    db.close()
    return res


def execute_fromfile(filename):
    db = pymysql.connect(host=HOST, port=int(PORT), user=USERNAME, password=PASSWORD, database=DATABASE,
                         charset='utf8mb4')
    fd = open(filename, 'r', encoding='utf-8')
    cursor = db.cursor()
    sqlfile = fd.read()
    sqlfile = sqlparse.format(sqlfile, strip_comments=True).strip()

    sqlcommamds = sqlfile.split(';')

    for command in sqlcommamds:
        try:
            cursor.execute(command)
            db.commit()

        except Exception as msg:

            db.rollback()
    db.close()


def init_db():
    if is_exist_database():
        print('数据库已经存在,为防止误初始化，请手动删除 %s 数据库' % str(DATABASE))
        return
    if init_database():
        print('数据库%s创建成功' % str(DATABASE))
    execute_fromfile('test/lnkunadmin.sql')
    print('表创建成功')
    print('欢迎使用lnkun-admin-flask,请使用 flask run 命令启动程序')
