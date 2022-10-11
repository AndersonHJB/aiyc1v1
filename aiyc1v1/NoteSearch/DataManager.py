# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 13:39
# @Author  : AI悦创
# @FileName: DataManager.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from uuid import uuid4
import json
import os

# 此库需要用到的 static variable
TEMPLATE_CONTENT = "FingerPrint={uuid};line:{index}>>>{content}"
# TEMPLATE_PATH = "FilePath:{path}"
TEMPLATE_CONTENT_WITH_PATH = "FilePath:{path}\n{content}"
DATA_FILE_PATH_DICT = {"DictPath": []}  # 构建存储成 json。


class DataManger(object):
    def __init__(self, path: str):
        self.path = path

    # ------------搜索器 start------------
    def postfix(self, path: str):
        """判断文件后缀"""
        suffix = path.split(".")[-1]
        sum_suffix = [
            "py", "xlsx", "xls", "html", "css", "js",
            "txt", "csv", "json", "md"
        ]
        # print(suffix)
        # return path, suffix
        if suffix in sum_suffix:
            return suffix.lower()
        else:
            return ""

    def general_read(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()
            # return f.read()

    def decide_suffix(self, path, suffix):
        """判断文件后缀，使用对应的函数打开文件"""
        if suffix == "py":
            # content_list = self.general_read(path)
            return self.general_read(path)
        elif suffix == "txt":
            return self.general_read(path)
        elif suffix == "md":
            return self.general_read(path)

    # ------------搜索器 end------------

    # ------------索引器 start------------
    def parse(self, content, path):
        global DATA_FILE_PATH_DICT
        uuid = str(uuid4())
        detail_dict_to_json_value = {uuid: path}
        # print(detail_dict_to_json_value)
        DATA_FILE_PATH_DICT["DictPath"].append(detail_dict_to_json_value)
        # json
        """清洗数据，清洗成方便后面索引的数据"""
        # content_lst = []
        # content_dict = {}
        line_content_str = ""
        # for i in self.general_read(path):
        #     print(i, end="")
        # # print(self.general_read(path))
        # print(self.general_read(path).index("# -*- coding: utf-8 -*-\n"))
        for line, content in enumerate(content):
            if content == "\n":
                continue
            line_content = TEMPLATE_CONTENT.format(uuid=uuid, index=line + 1, content=content)
            # print(line_content)
            # print("-------独立---------")
            line_content_str = line_content_str + line_content
            # print(line_content_str)
            # print(line_content, end="")
            # content = str(line + 1) + content
            # content = (line+1, TEMPLATE_CONTENT.format(index=line+1, content=content))
            # content_lst.append(content)
            # content_dict[line + 1] = TEMPLATE_CONTENT.format(index=line + 1, content=result_content)
            # print(content, end="")
            # print(result_content, end="")
            # print(dict(content_lst))
            # print(content_dict)
            # for value in content_dict.values():
            #     print(value, end="")
            # save(value)
        # path = TEMPLATE_PATH.format(path=self.path)
        return TEMPLATE_CONTENT_WITH_PATH.format(path=path, content=line_content_str)

    # def save_file(self, content):
    #     with open("NoteSearch_DataBase.txt", "a+", encoding="utf-8") as f:
    #         f.write(content + "\n")

    # ------------索引器 end------------

    def DataManager_Engine(self, path):
        suffix = self.postfix(path=path)
        # print(suffix)
        content = self.decide_suffix(path=path,
                                     suffix=suffix)
        # print(content)
        if content:
            return self.parse(content, path)
        else:
            return "很抱歉，系统检测到：你很空虚，所以说拜拜～哈哈哈～"
    def path_generate(self):
        """生成全部要检索的路径"""
        path_lst = []  # 路径全部放入列表
        for dirpath, dirnames, filenames in os.walk(self.path):
            # print(dirpath, dirnames, filenames)
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                # print(filepath)
                path_lst.append(filepath)
        return path_lst


# class DataSave(object):
#     def __int__(self, path):
#         self.path = path
