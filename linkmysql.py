#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 15:12
# @Email    : yangtianyu92@126.com
import pymysql.cursors
import random
import csv
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
        if table == "random_urls":
            pass
        else:
            url_list = link_mysql_read(sql_all_url.format(table))
            url_list_result.extend([(url["url"], table) for url in url_list])
    random.shuffle(url_list_result)
    return url_list_result


# 把随机url和对应table名称插入csv文件中，3万行大约6M，压缩后30万行大约6M，上传下载速度可以接受
def url_to_csv(urls):
    with open("./urlLists/url_list1.csv", 'w', newline='',encoding='utf-8') as f:
        fieldnames = ["url", "table_name"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for url in urls:
            writer.writerow({"url": url[0], "table_name": url[1]})


if __name__ == '__main__':
    urls = make_url_list_all_random()
    url_to_csv(urls)

