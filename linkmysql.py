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
            result = cursor.fetchall()
    finally:
        connection.close()
    return result


# 写入数据库或更改数据库
def link_mysql_write(sql):
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
        result = cursor.fetchall()
        connection.commit()
    finally:
        connection.close()
    return result


if __name__ == '__main__':
    sql_show_all = "show tables;"
    table_names = [name["Tables_in_test"] for name in link_mysql_read(sql_show_all)]
    print(table_names[0])
    sql_test = """
    alter table agri_hotspot add (
        `title` varchar(1200) DEFAULT NULL,
        `product` varchar(300) DEFAULT NULL,
        `brands` varchar(300) DEFAULT NULL,
        `Manufacturer` varchar(300) DEFAULT NULL,
        `Packageranddistributor` varchar(300) DEFAULT NULL,
        `Numbers` int(15) DEFAULT NULL,
        `html` MediumText DEFAULT NULL
    );
    """
    link_mysql_write(sql_test)

