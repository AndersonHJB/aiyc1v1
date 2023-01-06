# -*- coding: utf-8 -*-
# @Time    : 2023/1/6 17:51
# @Author  : AI悦创
# @FileName: SEARCH_ENGINE.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import re
from pprint import pprint


class Search_Engine():
    def __init__(self):
        # with open("SEARCH_DATA.txt", "r") as f:
        with open("SEARCH_DATA_NAME11.txt", "r") as f:
            self.search_data = f.read()

    def regex(self, query, search_data):
        # pattern = re.compile('FingerPrint', re.S)
        pattern = 'FingerPrint=(.*?);line:(\d+)>>>(.*?{query}.*)'.format(query=query)
        # pattern = 'FingerPrint=(.*?);line:(\d+)>>>.*?({query}.*?)'.format(query=query)
        print(pattern, "-------")
        # result = re.findall(pattern, search_data, re.S | re.I)
        result = re.findall(pattern, search_data)
        return result

    def search(self, user_search):
        print("正在运行")
        r = self.regex(user_search, self.search_data)
        pprint(r)

        # pattern = 'FingerPrint.*?=(.*?);line:(\d+)>>>.*?({query}).*?'

        # query = input(":>>>")
        # pattern = '.*?FilePath:(.*?).*?line:(\d+)>>>.*?(print).*?'
        # pattern = '.*?FilePath:(.*?).*?line:(\d+)>>>.*?({query}).*?'
        # print(pattern)
        # result = re.findall(pattern, content, re.S|re.I)
        # print(result)
