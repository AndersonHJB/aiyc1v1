# -*- coding: utf-8 -*-
# @Time    : 2023/1/6 17:51
# @Author  : AI悦创
# @FileName: SEARCH_ENGINE.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import json
import re
import time
from pprint import pprint

class Search_Engine():
    def __init__(self):
        with open("SEARCH_DATA.txt", "r", encoding="utf-8") as f:
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
        search_result = self.regex(user_search, self.search_data)
        path_list = self.json_load()
        self.generate_path_and_search(search_result, path_list)
        # print(r[0][0])
        # for p_d in path_list:
        #     # print(p_d)
        #     if p_d.get(search_result[0][0], None):
        #         path = p_d.get(search_result[0][0])
        #         print(path)
        # pprint(search_result)

    def json_load(self):
        with open("PATH_JSON.json", "r") as f:
            return json.load(f)["DictPath"]

        # pattern = 'FingerPrint.*?=(.*?);line:(\d+)>>>.*?({query}).*?'

        # query = input(":>>>")
        # pattern = '.*?FilePath:(.*?).*?line:(\d+)>>>.*?(print).*?'
        # pattern = '.*?FilePath:(.*?).*?line:(\d+)>>>.*?({query}).*?'
        # print(pattern)
        # result = re.findall(pattern, content, re.S|re.I)
        # print(result)

    def generate_path_and_search(self, search_result, path_list):
        if len(search_result) > 1:
            result_data = []
            for uuid, line, content in search_result:
                # print(uuid, line, content)
                for p_l in path_list:
                    if not p_l.get(uuid):
                        continue
                    result_data.append(p_l.get(uuid))
                    # if p_l.get(uuid):
                    #     result_data.append(p_l.get(uuid))
                    # continue
                    print(p_l.get(uuid), line, content)
            print(result_data)
            return result_data
        r = search_result[0]


