#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 15:12
# @Email    : yangtianyu92@126.com
import pymysql.cursors

# 链接数据库


# 读取数据库
def link_mysql_read(sql):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        print("sql processed")
    return result


# 写入数据库或更改数据库
def link_mysql_write(sql):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()
    except:
        raise BufferError
    finally:
        connection.close()
        print("sql processed")


# 显示所有表名
def show_tables():
    sql_show_all_fake = "show tables;"
    table_names_fake = [name[list(name.keys())[0]] for name in link_mysql_read(sql_show_all_fake)]
    return table_names_fake


if __name__ == '__main__':
    sql_show_all = "show tables;"
    table_names = [name[list(name.keys())[0]] for name in link_mysql_read(sql_show_all)]
    print(table_names)


