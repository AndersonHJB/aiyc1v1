import json

from aiyc1v1 import DataManger

abs_path = "/Users/huangjiabao/GitHub/PythonProject/aiyc1v1/aiyc1v1/NoteSearch"
d = DataManger(path=abs_path)
d.run()


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
