#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : __init__.py.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/10 15:28
"""

import os

import click

from applications.common.script.initdb import init_db
from applications.common.script.newmodular.new import NewViewModular


def init_script(app):
    @app.cli.command()  # 加上这个 直接执行 flask init 就可以初始化数据库了
    def init():
        init_db()

    @app.cli.command()  # 将该方法变成一个命令行工具
    @click.option('--type', prompt="请输入类型", help='新增的类型')  # 通过指定命令行选项的名称，从命令行读取参数值，再将其传递给函数
    @click.option('--name', prompt="请输入新增的名称", help='新增的名称')
    def new(type, name):
        # flask new --type view --name test/a
        if type == 'view':
            if name.count('/') > 1:
                print("目前只支持二级目录，多级目录需要蓝图嵌套，本命令暂不支持，请手动创建")
                quit()
            if type == "view" and os.path.exists(f"applications/view/{name}.py"):
                print(f'已经存在视图模块{name}.py')
                quit()
            NewViewModular(name=name).new_view()
