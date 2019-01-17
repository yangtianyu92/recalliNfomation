#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 11:38
# @Email    : yangtianyu92@126.com
from linkmysql import  link_mysql_read, link_mysql_write

sql_read = """ select ThirdReport_Content FROM unionnew2018.recall2018;"""

result = link_mysql_read(sql=sql_read)

for content in result:
    sql = """insert into recall2018()"""