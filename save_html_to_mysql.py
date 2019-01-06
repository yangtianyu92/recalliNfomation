#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 21:32
# @Email    : yangtianyu92@126.com
from linkmysql import link_mysql_write, link_mysql_read, show_tables, connection
from mulit_downloads import muliti_down
import pymysql.cursors

# 读表插入HTML字段当中
table_name = show_tables()

# 获取url列表
sql = "select * from {} limit 5;"
c_r = link_mysql_read(sql=sql.format(table_name[0]))
url_list = [data["url"] for data in c_r]


if __name__ == '__main__':
    print(c_r)
    print(url_list)
    connection.close()
    result = muliti_down(url_list)

    sql = ""

