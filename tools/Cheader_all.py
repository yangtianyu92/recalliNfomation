#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 20:58
# @Email    : yangtianyu92@126.com

import heapq
import pprint
import json

header_test = """
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8
Cache-Control: max-age=0
Connection: keep-alive
Cookie: td_cookie=1586371308; __gads=ID=6efab4d2cfdbf3dd:T=1545724958:S=ALNI_MYm731z5NsV_HMjjpwJOsP1eYQLJw; Hm_lvt_2aeaa32e7cee3cfa6e2848083235da9f=1545724899,1545724907,1547798446,1548218310; __51cke__=; yunsuo_session_verify=0a2f72261c6d64e8c7c14d6429c1f182; Hm_lpvt_2aeaa32e7cee3cfa6e2848083235da9f=1548223783; __tins__1636283=%7B%22sid%22%3A%201548223783146%2C%20%22vd%22%3A%201%2C%20%22expires%22%3A%201548225583146%7D; __51laig__=13
Host: news.foodmate.net
If-Modified-Since: Fri, 18 Jan 2019 07:22:44 GMT
If-None-Match: W/"5c417ec4-9c3d"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
"""


class HeaderMake:
    def __init__(self, header):
        self.header_resource = header
        self.headers = {}
        self.colon = []
        self.newline = []

    # 读取另起一行和之最近一个的冒号的符号位置
    def _read(self):
        colon_list = []
        newline_list = []
        header_resource = self.header_resource
        for index, char in enumerate(header_resource):
            if char == "\n":
                newline_list.append(index)
        for locate in newline_list:
            colon_index = header_resource.find(':', locate)
            if colon_index > 0:
                colon_list.append(colon_index)
        return colon_list, newline_list

    # 通过位置生成header词典
    def make(self):
        colon_list, newline_list = self._read()
        merge_list = list(heapq.merge(colon_list, newline_list))
        for index, local in enumerate(merge_list):
            if index % 2 != 0:
                self.headers[self.header_resource[merge_list[index - 1]:local].replace('\n', '')] = \
                    self.header_resource[local + 2:merge_list[index + 1]]
        return self.headers


if __name__ == '__main__':
    hm = HeaderMake(header_test)
    pprint.pprint(hm.make())

