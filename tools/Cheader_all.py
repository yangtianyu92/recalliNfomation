#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 20:58
# @Email    : yangtianyu92@126.com

import heapq
import pprint
import json

header_test = """
view_name: search_news_alerts_alerts
view_display_id: page_1
view_args: 
view_path: /views/ajax
view_base_path: news-alerts/search/alerts
view_dom_id: 966f44a754226ac64970313d77a168630987ef28e917c6ce1dea6cb7ccb50ffd
pager_element: 0
page: 17
_drupal_ajax: 1
ajax_page_state[theme]: fsa
ajax_page_state[theme_token]: 
ajax_page_state[libraries]: addtoany/addtoany,anchor_link/drupal.anchor_link,better_exposed_filters/auto_submit,better_exposed_filters/general,cookieconsent/cookieconsent-min,cookieconsent/settings,core/html5shiv,datalayer/behaviors,extlink/drupal.extlink,fsa/global,fsa_custom/add_to_any,fsa_custom/history_back,fsa_custom/page_print,fsa_es/accessibility,fsa_es/result_totals,fsa_gtm/data_layer.navref,fsa_gtm/data_layer.search,fsa_page_feedback/page_feedback,system/base,views/views.ajax,webform/webform.ajax,webform/webform.element.details.save,webform/webform.element.details.toggle,webform/webform.element.options,webform/webform.element.radios,webform/webform.form
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

