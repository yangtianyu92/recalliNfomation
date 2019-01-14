#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 16:17
# @Email    : yangtianyu92@126.com
from linkmysql import link_mysql_read, link_mysql_write
from save_html_to_mysql import base64_decode
from bs4 import BeautifulSoup
import requests
from mulit_downloads import header

sql_read_from_html = """
select result from agri_hotspot limit 20; 
"""

list_content = link_mysql_read(sql_read_from_html)

# for content in list_content:
html_test = base64_decode(list_content[9]['htmlContent'])


soup = BeautifulSoup(html_test, "lxml")

print(soup.title.text)
print(soup)
