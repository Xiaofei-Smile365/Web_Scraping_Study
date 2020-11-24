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
    

    end_time = time.time()
    start_end = end_time - start_time

    return start_end


if __name__ == '__main__':
    print("* [Start] for the Programe in %s\n" % datetime.datetime.now())
    consuming = main()
    print("* [End] for the Programe in %s\n" % datetime.datetime.now())
    print("[Program time consuming] is %s s" % consuming)

    pass
