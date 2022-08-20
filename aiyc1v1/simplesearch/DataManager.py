import pandas as pd


class DataManager(object):
    def __init__(self, path: str, ignore_postfix=[]):
        self.path = path
        # self.empty_content = ""
        self.content = ""
        self.ignore_postfix = ["zip", "png", "jpg", "jpge", "rar", "xml",
                               "html", "js", "css", "docx", "json", "gitignore",
                               "ipynb", "parquet", "jsx", "mp3"]
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
        if postfix == "txt" or postfix == "md":
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
            # self.empty_content = f.readlines()
            self.content = f.read()
            # return content, len(content)
            # return content

    def read_csv(self):
        """
        read csv
        """
        self.content = str(pd.read_csv(self.path))
        # return content

    def read_excel(self):
        self.content = str(pd.read_excel(self.path))
        # return content


class DataSearch(object):
    """存储搜索数据"""

    def __init__(self, datasearch):
        self.datasearch = datasearch

    def save(self):
        with open("DataSearch.txt", "a+", encoding="utf-8") as f:
        # with open("DataSearch.txt", "a+") as f:
            f.write(self.datasearch + "\n")
            # f.close()
