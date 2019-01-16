#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/7 22:28
# @Email    : yangtianyu92@126.com
import csv
from linkmysql import link_mysql_read

result = link_mysql_read("""SELECT * FROM unionnew2018.recall2018;""")
print(result)

"""
url_2018 = []
with open('./urlLists/url_list1.csv', 'r',newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if "2016" in row["url"]:
            url_2018.append(row)
"""

with open('./urlLists/recall2018.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ["url"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for dic in result:
        writer.writerow({"url": dic["ThirdReport_Url"]})
