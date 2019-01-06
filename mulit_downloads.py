#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/5 17:19
# @Email    : yangtianyu92@126.com
from multiprocessing import Pool
import requests
import time
from bs4 import BeautifulSoup
import re

header = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'cache-control': 'max-age=0',
 'cookie': '_ga=GA1.2.129905225.1540258197; _gid=GA1.2.379007114.1545049326; '
           '_ceg.s=pjxmog; _ceg.u=pjxmog; '
           '_4c_=jVPNbts8EHyVDzwHEkn9Ub6lTdP20gIpPhQ9CStyZRORRIOk5RpB3j1LRXHRQ4CeTO6MZne44yd2PuDMdqIqK1HURaOkrG%2FYI14C2z0xb036WdiOGawrNagWhC76thY9KOBSVC0MjeQ1Zzfs96qjeFGKVqlCPN8wfdy%2Bf2LaGSQd0WZFVhIb5yR79IbOA9GYkG3LKymrjFS4rJRoG8I%2B33Zf796HT34k8BDjMezy%2FHw%2BZ4OBbO%2BW%2FAcMGC%2F5A2oYx5AbHOA0xuwQp9TRObLGftHR%2BNOe3LJvdO6tG93e6tCPRFhAazvjG6hdmDASuH3owViI1s0dpvkTBWY7wbhgRG9n8JetHF1PUu7onTnp%2BKY3obE0m8HF6muT%2B7vb7gOE1y6pEFYbW0siarsBI4QYUKcBqHKfDNFrueUOR7vgtfcXN%2BER9untVzkErw9%2FXWjYKXWjwgPuTyNE5y%2Fd7TCA9W9ee%2B%2FOAT3dPh48Kf7XpI27BP%2B0syEwPQgO6P3KSguhfQjFM1E3WVlnUjS7inOeRwiPOS2poyV1aexuW9H3U%2Bw9wmP4NKHf46wthg3alrcTQnAFhZRcNbrig1JcIQ49tobXUGLyZGPyuqUgPf4fe8cUufo1VP%2B%2FnyoK7muWCZBVWbZNQzKRgqbqkixwToyktUab%2Fi%2F%2FwKbryhZXtihrIcqmpcrKFuXGfn5%2BAQ%3D%3D',
 'upgrade-insecure-requests': '1',
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}

urls = ["http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com","http://www.baidu.com", "http://www.sogou.com", "http://www.bing.com"]


# 清理html网页文件
def clear_html(html):
    soup = BeautifulSoup(html, 'lxml')
    clear_soup = re.sub('[\.\!\/_$%^*(\"\')—?【】“”！，。？、~@#￥…&（）\n\t\r;]', '', soup.text)
    return clear_soup


def get_html(url):
    response = requests.get(url, headers=header)
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