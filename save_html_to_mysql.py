#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 21:32
# @Email    : yangtianyu92@126.com
from linkmysql import link_mysql_write, link_mysql_read, show_tables, connection
from mulit_downloads import muliti_down, clear_html
import pymysql.cursors

# 读表插入HTML字段当中
table_name = show_tables()


if __name__ == '__main__':
    # 获取url列表
    sql = "select * from {};"
    c_r = link_mysql_read(sql=sql.format(table_name[6]))
    url_list = [data["url"] for data in c_r]

    # 多进程下载
    len_url = len(url_list)
    for i in range(10, len_url):
        url_piece = url_list[i*10:i*10+10]
        print(url_piece, i)
        result = muliti_down(url_piece)
        for html in result:
            sql = """update {0} set html = "{1}" where url="{2}";"""
            ch = clear_html(html[0])
            sql_raw = sql.format(table_name[6], pymysql.escape_string(ch), html[1])
            link_mysql_write(sql_raw)
        connection.close()
