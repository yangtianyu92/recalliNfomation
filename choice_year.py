#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 22:28
# @Email    : yangtianyu92@126.com
import csv
from linkmysql import link_mysql_read
import random

result = link_mysql_read("""SELECT * FROM criterion2018 where ThirdReport_SiteName="中国农业贸易政策";""")
print(result)

"""
url_2018 = []
with open('./urlLists/url_list1.csv', 'r',newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if "2016" in row["url"]:
            url_2018.append(row)
"""

with open('./urlLists/criterion2018.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ["url"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    sum_dic = [dic for dic in result]
    random.shuffle(sum_dic)
    for dic in sum_dic:
        writer.writerow({"url": dic["ThirdReport_Url"]})
