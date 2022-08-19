class DataManager():
    def __init__(self, path):
        self.path = path
        self.empty_content = ""

    def postfix(self):
        """
        解析路径后缀，并调用指定文件读取方法
        """
        postfix = self.path.split(".")[-1]
        # print(postfix)
        if postfix == "txt":
            self.read_file(self.path)
        elif postfix == "py":
            self.read_file(self.path)
        elif postfix == "csv":
            self.read_csv(self.path)

    def read_file(self, path):
        """
        read file general
        通用文件打开函数
        """
        with open(path, "r", encoding="utf-8") as f:
            content = f.readlines()
            return content, len(content)

    def read_csv(self, path):
        """
        read csv
        """
        import pandas as pd
        content = pd.read_csv(self.path)
        return content
