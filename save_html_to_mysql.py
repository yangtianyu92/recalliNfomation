#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 21:32
# @Email    : yangtianyu92@126.com
from linkmysql import link_mysql_write, link_mysql_read, show_tables, connection
from mulit_downloads import muliti_down, get_html, clear_html
import pymysql.cursors
from bs4 import BeautifulSoup
import re

# 读表插入HTML字段当中
table_name = show_tables()


if __name__ == '__main__':
    # 获取url列表
    sql = "select * from {} limit 10;"
    c_r = link_mysql_read(sql=sql.format(table_name[0]))
    url_list = [data["url"] for data in c_r]

    # 多进程下载
    result = muliti_down(url_list)
    for html in result:
        sql = """update {0} set html = "{1}" where url="{2}";"""
        ch = clear_html(html[0])
        sql_raw = sql.format(table_name[0], pymysql.escape_string(ch), html[1])
        link_mysql_write(sql_raw)
        print(sql_raw)
    connection.close()
