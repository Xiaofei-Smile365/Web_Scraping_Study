# -*- coding: UTF-8 -*-

"""

@Project Name: Web_Scraping_Study
@File Name:    TXT_Save

@User:         smile
@Author:       Smile
@Email:        Xiaofei.Smile365@Gmail.com

@Date Time:    2020/11/24 11:04
@IDE:          PyCharm

"""

import time
import datetime


def main():
    start_time = time.time()
    print("--- Here is main code! ---\n")
    import requests
    from pyquery import PyQuery as pq
    import requests
    from lxml import etree
    from requests.auth import HTTPBasicAuth
    from lxml import etree

    url_auo = 'https://www.auo.com/zh-CN'

    response_auo = requests.get(url_auo)
    html_text_auo = response_auo.text

    html_auo = etree.HTML(html_text_auo)
    text_auo_site_map = html_auo.xpath('//*[@id="footer_block"]/div[1]/div/table/tr/td[1]/ul/li[1]/a/text()')

    if '网站地图' in text_auo_site_map[0]:
        url_auo_site_map = url_auo[0:19] + html_auo.xpath('//*[@id="footer_block"]/div[1]/div/table/tr/td[1]/ul/li[1]/a/@href')[0]

        response_auo_site_map = requests.get(url_auo_site_map)
        html_text_auo_site_map = response_auo_site_map.text

        html_auo_site_map = etree.HTML(html_text_auo_site_map)
        html_auo_site_map_url_list = []
        for m in range(0, 10):
            for n in range(0, 10):
                try:
                    text_auo_site_map_text = html_auo_site_map.xpath('//*[@id="main_content"]/ul[%s]/li[%s]/a/text()' % ((m + 1), (n + 1)))[0].strip()
                    text_auo_site_map_url = url_auo[0:19] + html_auo_site_map.xpath('//*[@id="main_content"]/ul[%s]/li[%s]/a/@href' % ((m + 1), (n + 1)))[0]
                    html_auo_site_map_url_list.append([text_auo_site_map_text, text_auo_site_map_url])
                except Exception as e:
                    print("The Error in %s is [%s]" % (datetime.datetime.now(), e), "\n")
                    pass
        print(html_auo_site_map_url_list, "\n")

        # Sample：关于友达光电
        response_auo_site_map_about_auo_html = requests.get(html_auo_site_map_url_list[0][1])
        html_text_auo_site_map_about_auo_text = response_auo_site_map_about_auo_html.text
        html_auo_site_map_about_auo_text = etree.HTML(html_text_auo_site_map_about_auo_text)
        print(html_auo_site_map_about_auo_text.xpath('//*[@id="main_content"]/div/table[1]/tbody/tr/td/text()'))

    end_time = time.time()
    start_end = end_time - start_time

    return start_end


if __name__ == '__main__':
    print("* [Start] for the Program in %s\n" % datetime.datetime.now())
    consuming = main()
    print("* [End] for the Program in %s\n" % datetime.datetime.now())
    print("[Program time consuming] is %s s" % consuming)

    pass
