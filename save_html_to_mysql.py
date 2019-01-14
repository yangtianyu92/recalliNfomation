#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 21:32
# @Email    : yangtianyu92@126.com
from linkmysql import link_mysql_write, link_mysql_read, show_tables
from mulit_downloads import muliti_down, clear_html, get_html
import pymysql.cursors
import base64
import csv

# 读表插入数据库表内HTML字段当中
table_name = show_tables()


# 编码
def base64_encode(c):
    return base64.b64encode(c.encode("utf-8")).decode("utf-8")


# 解码
def base64_decode(c):
    return base64.b64decode(c).decode("utf-8")


# 把当前行数记录在url_num_count.txt文件中，如果内存溢出，或者网络中断，可以继续下载
def save_index(index):
    with open(r'C:\Users\888\PycharmProjects\recall0Information\urlLists\2018count.txt','w', encoding='utf-8') as f:
        f.write(str(index))


# 读取index值
def read_index():
    with open(r'C:\Users\888\PycharmProjects\recall0Information\urlLists\2018count.txt', 'r', encoding='utf-8') as f:
        number = f.read()
    return int(number)


# 读取csv中所有的url
def get_all_url(file):
    url_list = []
    with open(file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for index, row in enumerate(reader):
            url_list.append((row["url"], row["table_name"]))
    return url_list


# save html file to sql
def save_html(urls):
    index_begin = read_index()
    url_list = urls[index_begin:]
    for index1, url_temp in enumerate(url_list):
        if url_temp[1] == "heath_canada_recall":
            continue
        print(url_temp)
        response = get_html(url_temp[0])
        sql = """update {0} set html = "{1}" where url="{2}";"""
        sql_content = """update {0} set htmlContent = "{1}" where url="{2}";"""
        ch_base64 = base64.b64encode(response[0].encode('utf-8')).decode('utf-8')
        ch_base64_sql = sql_content.format(url_temp[1], ch_base64, url_temp[0])
        link_mysql_write(ch_base64_sql)
        ch = clear_html(response[0])
        try:
            sql_raw = sql.format(url_temp[1], pymysql.escape_string(ch), url_temp[0])
            link_mysql_write(sql_raw)
        except:
            response = get_html(url_temp[0], encode="gbk")
            ch = clear_html(response[0])
            sql_raw = sql.format(url_temp[1], pymysql.escape_string(ch), url_temp[0])
            link_mysql_write(sql_raw)
        save_index(index_begin + index1 + 1)
        print(index_begin + index1 + 1)


if __name__ == '__main__':
    urls = get_all_url("C:\\Users\\888\\PycharmProjects\\recall0Information\\urlLists\\url_list4_2018.csv")
    save_html(urls=urls)
    '''    # 获取url列表
    sql = "select * from {};"
    c_r = link_mysql_read(sql=sql.format(table_name[6]))
    url_list = [data["url"] for data in c_r]

    # 多进程下载
    len_url = len(url_list)
    for i in range(425, len_url):
        url_piece = url_list[i*10:i*10+10]
        print(url_piece, i)
        result = muliti_down(url_piece)
        for html in result:
            sql = """update {0} set html = "{1}" where url="{2}";"""
            sql_content = """update {0} set htmlContent = "{1}" where url="{2}";"""
            ch_base64 = base64.b64encode(html[0].encode('utf-8')).decode('utf-8')
            ch_base64_sql = sql_content.format(table_name[6], ch_base64, html[1])
            link_mysql_write(ch_base64_sql)
            ch = clear_html(html[0])
            sql_raw = sql.format(table_name[6], pymysql.escape_string(ch), html[1])
            link_mysql_write(sql_raw)
'''