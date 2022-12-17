# -*- coding: utf-8 -*-
# @Time    : 2022/12/17 14:52
# @Author  : AI悦创
# @FileName: demo.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import json
with open("path.json", "r") as f:
    content = json.load(f)
# print(content["DictPath"])
# print(type(content))
for d in content["DictPath"]:
    # print(d)
    print(d.get("e1d68f6a-1cc2-4d22-9bed-e9be5596ada5"), "未找到")
# ------------------------------------------------------------
with open("wyh_json/data.txt", "r") as f:
    # content = f.readlines()
    content = f.read()
# print(len(content))

lst = []
for i in content.split(","):
    n1 = i.find("[")
    n2 = i.find("]")
    # print(i.find("["))
    if (n1 == -1) and (n2 == -1):
        # print(i)
        lst.append(i)
    else:
        if not (n1 == -1):
            new_i = i[i.find("[") + 1:]
            # print(new_i)
            lst.append(new_i)
        else:
            r = i[:n2]
            # print(r)
            lst.append(r)
u = input(":>>>")
for i in lst:
    i = i.replace("{", "")
    i = i.replace("}", "")
    i = i.replace('"', "")
    i = i.replace(' ', "")
    # i = i.strip(" ")
    if u in i:
        print(i.split(":")[1])
# ["e1d68f6a-1cc2-4d22-9bed-e9be5596ada5"]
