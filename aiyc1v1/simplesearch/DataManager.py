class DataManager(object):
    def __init__(self, path: str):
        self.path = path
        self.empty_content = ""

    def postfix(self):
        """
        解析路径后缀，并调用指定文件读取方法
        """
        postfix = self.path.split(".")[-1]
        # print(postfix)
        if postfix == "txt":
            self.read_file()
        elif postfix == "py":
            self.read_file()
        elif postfix == "csv":
            self.read_csv()

    def read_file(self):
        """
        read file general
        通用文件打开函数
        """
        with open(self.path, "r", encoding="utf-8") as f:
            content = f.readlines()
            return content, len(content)

    def read_csv(self):
        """
        read csv
        """
        import pandas as pd
        content = pd.read_csv(self.path)
        return content
