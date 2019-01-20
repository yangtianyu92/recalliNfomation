#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/20 18:01
# @Email    : yangtianyu92@126.com
import requests
import json
import re
from linkmysql import link_mysql_write
import datetime
from tools.change_time_str import ChangeTime
from tools.clearAttr2 import clear_atr

header = {'accept': 'application/json, text/javascript, */*; q=0.01',
 'accept-encoding': 'gzip, deflate, br',
 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
 'content-length': '1097',
 'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
 'cookie': '__cfduid=d10182ee06f7ed97a0d41d5ebad1203b11547978364; '
           '_ga=GA1.3.981128867.1547978302; _gid=GA1.3.754703001.1547978302; '
           '_dc_gtm_UA-54078849-1=1',
 'origin': 'https://www.food.gov.uk',
 'referer': 'https://www.food.gov.uk/news-alerts/search/alerts',
 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
 'x-requested-with': 'XMLHttpRequest'}

url_uk = "https://www.food.gov.uk/views/ajax?_wrapper_format=drupal_ajax"


for i in range(21):
    form_dic = {'_drupal_ajax': '1',
     'ajax_page_state[libraries]': 'addtoany/addtoany,anchor_link/drupal.anchor_link,better_exposed_filters/auto_submit,better_exposed_filters/general,cookieconsent/cookieconsent-min,cookieconsent/settings,core/html5shiv,datalayer/behaviors,extlink/drupal.extlink,fsa/global,fsa_custom/add_to_any,fsa_custom/history_back,fsa_custom/page_print,fsa_es/accessibility,fsa_es/result_totals,fsa_gtm/data_layer.navref,fsa_gtm/data_layer.search,fsa_page_feedback/page_feedback,system/base,views/views.ajax,webform/webform.ajax,webform/webform.element.details.save,webform/webform.element.details.toggle,webform/webform.element.options,webform/webform.element.radios,webform/webform.form',
     'ajax_page_state[theme]': 'fsa',
     'ajax_page_state[theme_token]': '',
     'page': '',
     'pager_element': '0',
     'view_args': '',
     'view_base_path': 'news-alerts/search/alerts',
     'view_display_id': 'page_1',
     'view_dom_id': '966f44a754226ac64970313d77a168630987ef28e917c6ce1dea6cb7ccb50ffd',
     'view_name': 'search_news_alerts_alerts',
     'view_path': '/views/ajax'}

    form_dic["page"] = str(i)

    response = requests.post(url=url_uk, headers=header, data=form_dic)
    print(response.json())
    response_text = response.json()[2]['data']
    create_time = re.findall('<span class="field field__created">(.*?)</span>', response_text)
    ct = [ChangeTime(time, "%d %B %Y").mysql_time(3) for time in create_time]

    hrefs =["https://www.food.gov.uk" + href for href in re.findall('<a href=\"(.*?)\" rel="bookmark"><span class="field field__title">', response_text)]

    titles = [clear_atr(title) for title in re.findall('field__title">(.*)</span>', response_text)]
    print(ct, hrefs, titles)

    website_name = "英国食品标准局"

    datetime_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(i)
    for j in range(len(ct)):
        sql_raw = """insert into recall2018 (ThirdReport_Title, ThirdReport_Url, ThirdReport_CreateTime,\
        ThirdReport_GetherTime, ThirdReport_SiteName, ThirdReport_InfoType) values
        ("{0}", "{1}", "{2}", "{3}", "{4}", "{5}");
        """
        if "2018" in ct[j] or "2019" in ct[j]:
            a1 = sql_raw.format(titles[j], hrefs[j],  ct[j], datetime_now, website_name, "召回")
            link_mysql_write(a1)
