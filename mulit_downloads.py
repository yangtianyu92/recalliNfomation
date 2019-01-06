#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 17:19
# @Email    : yangtianyu92@126.com
from multiprocessing import Pool
import requests
import time

urls = ["http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com"]


def get_html(url):
    response = requests.get(url)
    response.encoding = "utf-8"
    return response.text, url


def muliti_down(urls):
    muliti_pool = Pool(10)
    result_html_list = muliti_pool.map(get_html, urls)
    return result_html_list


"""
让我们测试下多进程的优势，下载速度提升了60%
"""


if __name__ == '__main__':

    time_begin = time.time()
    for url in urls:
        print(get_html(url))
    time_end = time.time()
    print("time is ~~~~~---" + str(time_end - time_begin))