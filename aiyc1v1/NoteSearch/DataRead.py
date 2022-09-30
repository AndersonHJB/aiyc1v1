# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 13:39
# @Author  : AI悦创
# @FileName: DataRead.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
import pandas as pd

# 此库需要用到的 static variable
TEMPLATE_CONTENT = "line:{index}:{content}"

class DataRead(object):
    def __init__(self, path: str):
        self.path = path

    def postfix(self, path: str):
        """判断文件后缀"""
        suffix = path.split(".")[-1]
        sum_suffix = [
            "py", "xlsx", "xls", "html", "css", "js",
            "txt", "csv", "json"
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
            content_list = self.general_read(path)
            # for i in self.general_read(path):
            #     print(i, end="")
            # # print(self.general_read(path))
            # print(self.general_read(path).index("# -*- coding: utf-8 -*-\n"))
            for line, content in enumerate(content_list):
                if content == "\n":
                    continue
                # content = str(line + 1) + content
                # print(content, end="")
                print("Xxxxx")


    def main(self):
        suffix = self.postfix(path=self.path)
        # print(suffix)
        self.decide_suffix(path=self.path,
                           suffix=suffix)

# if __name__ == '__main__':
#     abs_path = r"/Users/huangjiabao/GitHub/aiyc1v1/aiyc1v1/NoteSearch/README.md"
#     d = DataRead(abs_path)
