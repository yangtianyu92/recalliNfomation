#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 20:58
# @Email    : yangtianyu92@126.com

import heapq
import pprint
import json

header_test = """
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8
cache-control: max-age=0
cookie: __cfduid=d10182ee06f7ed97a0d41d5ebad1203b11547978364; _ga=GA1.3.981128867.1547978302; _gid=GA1.3.754703001.1547978302; cookieconsent_dismissed=yes; _dc_gtm_UA-54078849-1=1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
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

