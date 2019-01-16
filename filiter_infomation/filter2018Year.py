#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 16:17
# @Email    : yangtianyu92@126.com
from linkmysql import link_mysql_read, link_mysql_write
from save_html_to_mysql import base64_decode
from bs4 import BeautifulSoup
import requests
from mulit_downloads import header
import json
import csv

sql_read_from_html = """
select result from agri_hotspot limit 20; 
"""

list_content = link_mysql_read(sql_read_from_html)

# for content in list_content:
html_test = list_content[0]["result"]

print(json.loads(html_test.decode('utf-8')))


# 对blob字段进行检查
def decode_result(raw):
    return json.loads(raw.decode('utf-8'))


def read_result():
    with open('../urlLists/url_list1.csv', 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader]
        for row in rows[:3]:
            sql = """select * from {0} where url="{1}";""".format(row["table_name"], row["url"])
            print(sql)
            result = link_mysql_read(sql)
            print(result)
            print("2018" in result["创建时间"])

read_result()