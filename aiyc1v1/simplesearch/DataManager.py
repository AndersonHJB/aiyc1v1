import pandas as pd


class DataManager(object):
    def __init__(self, path: str, ignore_postfix=[]):
        self.path = path
        self.empty_content = ""
        self.ignore_postfix = ["zip", "png", "jpg", "jpge", "rar", "xml"]
        self.ignore_postfix.extend(ignore_postfix)

    def postfix(self):
        """
        解析路径后缀，并调用指定文件读取方法
        """
        postfix = self.path.split(".")[-1]
        if postfix in self.ignore_postfix:
            return None
        # print(postfix)
        # else:
        if postfix == "txt":
            self.read_file()
        elif postfix == "py":
            self.read_file()
        elif postfix == "csv":
            self.read_csv()
        elif postfix == "xlsx" or postfix == "xls":
            self.read_excel()

    def read_file(self):
        """
        read file general
        通用文件打开函数
        """
        with open(self.path, "r", encoding="utf-8") as f:
            self.empty_content = f.readlines()
            # return content, len(content)
            # return content

    def read_csv(self):
        """
        read csv
        """
        self.empty_content = pd.read_csv(self.path)
        # return content

    def read_excel(self):
        self.empty_content = pd.read_excel(self.path)
        # return content
