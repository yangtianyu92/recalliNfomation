#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/14 16:17
# @Email    : yangtianyu92@126.com
from linkmysql import link_mysql_read, link_mysql_write
from save_html_to_mysql import base64_decode
from bs4 import BeautifulSoup
import re
import requests
from filiter_infomation.clearAttr import clear_atr

sql_read_from_html = """
select ThirdReport_Raw from recall2018 where ThirdReport_SiteName = "美国食品药品管理局网站" limit 1; 
"""

list_content = link_mysql_read(sql_read_from_html)


html_test = base64_decode(list_content[0]['ThirdReport_Raw'])

article = re.findall('<div class="col-md-9">(.*)<div class="table-responsive">', html_test, re.S)
print(article[0])

print(clear_atr(article[0]))


# print(soup.find_all(class_=))