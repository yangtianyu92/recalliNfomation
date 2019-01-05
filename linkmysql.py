#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 15:12
# @Email    : yangtianyu92@126.com
import pymysql.cursors

# 链接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# 读取数据库
def link_mysql_read(sql):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
    finally:
        connection.close()

# 写入数据库或更改数据库
def link_mysql_write(sql):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()
    finally:
        connection.close()

if __name__ == '__main__':
    