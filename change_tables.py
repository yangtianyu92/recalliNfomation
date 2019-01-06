#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 15:57
# @Email    : yangtianyu92@126.com
import pymysql.cursors
from linkmysql import link_mysql_read, link_mysql_write
# 链接数据库
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# 增加字段语句
sql = """
alter table {} add (
    `title` varchar(1200) DEFAULT NULL,
    `product` varchar(300) DEFAULT NULL,
    `brands` varchar(300) DEFAULT NULL,
    `Manufacturer` varchar(300) DEFAULT NULL,
    `Packageranddistributor` varchar(300) DEFAULT NULL,
    `Numbers` int(15) DEFAULT NULL,
    `html` MediumText DEFAULT NULL
);
"""

sql_html_content = """
alter table {} add (
    `htmlContent` MediumBlob DEFAULT NULL
);
"""

sql_show_all = "show tables;"
# 返回所有的数据库内的表名
table_names = [name["Tables_in_test"] for name in link_mysql_read(sql_show_all)]


if __name__ == '__main__':
    for table_name in table_names:
        link_mysql_write(sql_html_content.format(table_name))

    connection.close()
    print("all tables was processed")