class DataManager():
    def __init__(self, path):
        self.path = path
        self.empty_content = ""

    def postfix(self):
        """
        解析路径后缀，并调用指定文件读取方法
        """
        postfix = self.path.split(".")[-1]
        print(postfix)
