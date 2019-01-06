#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 21:32
# @Email    : yangtianyu92@126.com
from linkmysql import link_mysql_write, link_mysql_read, show_tables, connection
from mulit_downloads import muliti_down, get_html
import pymysql.cursors
from bs4 import BeautifulSoup
import html

# 读表插入HTML字段当中
table_name = show_tables()

# 获取url列表
sql = "select * from {} limit 5;"
c_r = link_mysql_read(sql=sql.format(table_name[0]))
url_list = [data["url"] for data in c_r]


if __name__ == '__main__':
    # 多进程下载
    #result = muliti_down(url_list)
    result = get_html(url_list[0])
    soup = BeautifulSoup(result[0], "lxml")
    sql = """update {0} set html = "{1}" where url="{2}";"""
    cc = html.escape(soup.text.replace(';', '').replace('\n','')).replace('\t','').replace('\n','').replace(' ', '')
    sql_raw = sql.format(table_name[0], (soup.text.replace(';', '').replace(' ', '').replace('\t','').replace('\n','')), result[1])
    print(cc)

