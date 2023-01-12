import json
import os

from aiyc1v1 import DataManger, Search_Engine

# abs_path = "/Users/huangjiabao/GitHub/PythonProject/aiyc1v1/aiyc1v1/NoteSearch"
abs_path = "/Users/huangjiabao/GitHub/WebSite/Bornforthis.cn/docs/column"
d = DataManger(path=abs_path)
d.run()

s = Search_Engine(language="zh_0CN")
s.search("专栏")
# import locale
# print(locale.getdefaultlocale())

# from aiyc1v1 import DelayWait

# r = os.path.exists("search_data.txt")
# print(r)
# import os
# os.remove("search_data.txt")

# s = "{}"
# path_lst = d.path_generate()
# # print(path_lst)
# for path in path_lst:
#     r = d.DataManager_Engine(path)
# print("xxxx", r)
# content = d.DataManager_Engine()
# print(content)
import re
# query = input(":>>>")
# pattern = '.*?FilePath:(.*?).*?line:(\d+)>>>.*?(print).*?'
# pattern = '.*?FilePath:(.*?).*?line:(\d+)>>>.*?({query}).*?'
# print(pattern)
# result = re.findall(pattern, content, re.S|re.I)
# print(result)
# lst = [1, 2, 3, 4, "\n", "dededed"]
#
# for content in lst:
#     if content == "\n":
#         print("if")
#         # continue
#         break
#     # content = str(line + 1) + content
#     # print(content, end="")
#     print(f"{content}Xxxxx")
