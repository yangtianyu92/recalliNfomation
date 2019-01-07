#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 15:12
# @Email    : yangtianyu92@126.com
import pymysql.cursors
import random
# 链接数据库


# 读取数据库
def link_mysql_read(sql):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
    finally:
        connection.close()
        print("sql processed")
    return result


# 写入数据库或更改数据库
def link_mysql_write(sql):
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='root',
                                 db='test',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql)
        connection.commit()
    except:
        raise BufferError
    finally:
        connection.close()
        print("sql processed")


# 显示所有表名
def show_tables():
    sql_show_all_fake = "show tables;"
    table_names_fake = [name[list(name.keys())[0]] for name in link_mysql_read(sql_show_all_fake)]
    return table_names_fake


def make_url_list_all_random():
    url_list_result = []
    """
    获取数据库内所有的url 相应的表名
    :return:
    """
    table_names = show_tables()
    sql_all_url = """select url from {};"""
    for table in table_names:
        print(table)
        url_list = link_mysql_read(sql_all_url.format(table))
        url_list_result.extend([(url["url"], table) for url in url_list])
    random.shuffle(url_list_result)
    return url_list_result


# 把随机url插入
def url_to_database(urls):
    sql = """insert into random_urls (url, table_name) values ("{}", "{}");"""
    for url in urls:
        sql_insert = sql.format(url[0], url[1])
        link_mysql_write(sql_insert)


if __name__ == '__main__':
    urls = make_url_list_all_random()
    url_to_database(urls)

