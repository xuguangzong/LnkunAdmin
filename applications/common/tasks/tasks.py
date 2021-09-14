#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
"""
@Project : LnkunAdmin
@File : tasks.py
@IDE : PyCharm
@Author : 小生爱吃窝窝头
@Date : 2021/9/13 14:02
"""
import datetime

task_list = ['task2', 'task3', 'task4']


def task2(a, b):
    print(f'定时任务_1_{a},{b},{datetime.datetime.now()}')


def task3(a, b):
    print(f'定时任务_2_{a}{b}{datetime.datetime.now()}')


def task4(a, b):
    print(f'定时任务_4_{a}{b}{datetime.datetime.now()}')
