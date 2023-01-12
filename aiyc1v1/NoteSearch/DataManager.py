# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 13:39
# @Author  : AI悦创
# @FileName: DataManager.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
from pprint import pprint
from uuid import uuid4
import json
import os

# 此库需要用到的 static variable
TEMPLATE_CONTENT = "FingerPrint={uuid};line:{index}>>>{content}"
# TEMPLATE_PATH = "FilePath:{path}"
TEMPLATE_CONTENT_WITH_PATH = "FilePath:{path}\n{content}"
DATA_FILE_PATH_DICT = {"DictPath": []}  # 构建存储成 json。
SEARCH_DATA_FILENAME = "SEARCH_DATA.txt"
PATH_JSON_FILENAME = "PATH_JSON.json"

class DataManger(object):
    def __init__(self, path: str):
        self.path = path
        self.run()


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
        """通用文件读取"""
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
        global DATA_FILE_PATH_DICT  # 全局字典，便于后期存储成 json 文件
        uuid = str(uuid4())
        detail_dict_to_json_value = {uuid: path}
        # print(detail_dict_to_json_value)
        DATA_FILE_PATH_DICT["DictPath"].append(detail_dict_to_json_value)
        # json
        """清洗数据，清洗成方便后面索引的数据"""
        line_content_str = ""
        # line_content_str = str()
        for line, content in enumerate(content):
            if content == "\n":
                continue
            line_content = TEMPLATE_CONTENT.format(uuid=uuid, index=line + 1, content=content)
            # line_content = "FingerPrint={uuid};line:{index}>>>{content}".format(uuid=uuid, index=line + 1, content=content)
            # print(line_content)
            # line_content 自动换行
            line_content_str = line_content_str + line_content
        # print("xxxxxxxx", line_content_str)

            # print(TEMPLATE_CONTENT_WITH_PATH.format(path=path, content=line_content_str))
            # print("-"*100)
        # "FilePath:{path}\n{content}"
        return TEMPLATE_CONTENT_WITH_PATH.format(path=path, content=line_content_str)

    # ------------索引器 end------------

    def data_manager_engine(self, path):
        suffix = self.postfix(path=path)
        # print(suffix)
        content = self.decide_suffix(path=path,
                                     suffix=suffix)  # 读取到文件内容
        # print(content)
        if content:
            return self.parse(content, path)  # 解析读取到的内容，并构建所需要的格式
        else:
            return f"Path:{path},很抱歉，系统检测到：你很空虚，所以说拜拜～哈哈哈～"

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

    def save_txt(self, filename, content):
        with open(filename, "a+", encoding="utf-8") as f:
            f.write(content + "\n")

    def save_json(self, filename, content):
        with open(filename, "a+", encoding="utf-8") as f:
            json.dump(content, f)

    def run(self):
        """
        code engine
        """
        path_lst = self.path_generate()  # 生成所有文件路径，返回列表类型
        # print(path_lst)
        if os.path.exists(SEARCH_DATA_FILENAME):
            os.remove(SEARCH_DATA_FILENAME)
        if os.path.exists(PATH_JSON_FILENAME):
            os.remove(PATH_JSON_FILENAME)
        for path in path_lst:
            content = self.data_manager_engine(path)  # 每个文件路径去读取、解析
            # print(type(content))
            # print(content)
            # print("-" * 100)
            self.save_txt(SEARCH_DATA_FILENAME, content)
        self.save_json(PATH_JSON_FILENAME, DATA_FILE_PATH_DICT)
        # pprint(DATA_FILE_PATH_DICT)
        # print(DATA_FILE_PATH_DICT)
        # with open("path.json", "w", encoding="utf-8")as f:
        #     json.dump(DATA_FILE_PATH_DICT, f)
# class DataSave(object):
#     def __int__(self, path):
#         self.path = path
