# -*- coding: utf-8 -*-
# @Time    : 2022/9/28 13:39
# @Author  : AI悦创
# @FileName: DataRead.py
# @Software: PyCharm
# @Blog    ：https://bornforthis.cn/
class DataRead(object):
    def __init__(self, path: str):
        self.path = path

    def postfix(self, path: str):
        """判断文件后缀"""
        suffix = path.split(".")[-1]
        # print(suffix)
        # return path, suffix
        return suffix

    def decide_suffix(self):
        """判断文件后缀，使用对应的函数打开文件"""

    def main(self):
        suffix = self.postfix(path=self.path)
        print(suffix)


# if __name__ == '__main__':
#     abs_path = r"/Users/huangjiabao/GitHub/aiyc1v1/aiyc1v1/NoteSearch/README.md"
#     d = DataRead(abs_path)
