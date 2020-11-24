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

    url = 'https://zhihu.com/explore'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    html = requests.get(url, headers=headers).text
    doc = pq(html)
    items = doc('.explore-tab .feed-item').items()
    for item in items:
        question = item.find('h2').text()
        author = item.find('.author-link-line').text()
        answer = pq(item.find('.content').html()).text()
        file = open('./source_file/explore.txt', 'a', encoding='utf-8')
        file.write('\n'.join[question, author, answer])
        file.write('\n' + '=' * 50 + '\n')
        file.close()

    end_time = time.time()
    start_end = end_time - start_time

    return start_end


if __name__ == '__main__':
    print("* [Start] for the Programe in %s\n" % datetime.datetime.now())
    consuming = main()
    print("* [End] for the Programe in %s\n" % datetime.datetime.now())
    print("[Program time consuming] is %s s" % consuming)

    pass
