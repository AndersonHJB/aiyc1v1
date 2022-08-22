import os
# from DataManager import DataManager
from aiyc1v1.simplesearch.DataManager import DataManager, DataSearch
import platform

DEFAULT_PATH = "/Users/huangjiabao/GitHub/MacBookPro16-Code/PythonCoder/StudentCoder"


class SimpleSearch():
    """
    简易文本搜索器
    一、交互
    1. 获取用户输入
        1.1 获取用户要查询的路径
            1.1.1 新路径
            1.1.2 默认路径
        1.2 获取用户要查询的内容
    二、结果
    1. 查询到结果则返回结果「该文件路径」和部分内容「前100字」
        1.1 并提示是否自动打开文件
        1.2 打开错误则返回报错信息
    2. 无结果则返回提示
    3. 询问是否继续查询
        4.1 继续查询输入 1
        4.2 结束查询输入 0
    三、特殊功能
    1. 每次程序启动询问是否要生成新的检索文件「意为："生成数据库"」——update
        1.1 up:更新
        1.2 noup:不更新
    扩展:
    1. 简易文件下载器
    2. GUI or web
    3.
    """

    def __init__(self):
        pass

    def path_generate(self, path: str):
        path_lst = []
        for dirpath, dirnames, filenames in os.walk(path):
            # print(dirpath, dirnames, filenames)
            for filename in filenames:
                # print(dirpath + filename)
                if platform.system().lower() == "windows":
                    path_lst.append(dirpath + "\\" + filename)
                else:
                    path_lst.append(dirpath + "/" + filename)
        return path_lst

    def path_diy_default(self):
        """
        判断用户选择默认路径还是填写自定义路径
        默认路径处理方法：1 or 直接回车
        """
        # default_path = "/Users/huangjiabao/GitHub/MacBookPro16-Code/PythonCoder/StudentCoder"
        tips = "请输入您想要查询的路径:\n" \
               ">>> 1 # 输入 1 或者\"直接 enter\"\n" \
               ">>> 直接输入您的路径\n" \
               ":>>>"
        user_path_input = input(tips)
        template = "您选择使用路径:%s, \n如果确认请输入回车或者 yes(否则:no):"
        if user_path_input == "" or user_path_input == "1":
            sure = input(template % DEFAULT_PATH)
            if sure == "" or sure.lower() == "yes":
                return DEFAULT_PATH
            else:
                return "Bye~"
        else:
            # user_path_input = input(tips)
            sure = input(template % user_path_input)
            if sure == "" or sure.lower() == "yes":
                return user_path_input
            else:
                return "Bye~"

    def read_to_save(self, path_list: list):
        u = input("是否要更新检索数据？")
        for path in path_list:
            print("PATH:>>>", path)
            datamanager = DataManager(path)
            datamanager.postfix()
            print(datamanager.content)
            datasearch = DataSearch(datamanager.content).save()


    def main(self):
        path = self.path_diy_default()
        # path = "/Users/huangjiabao/GitHub/MacBookPro16-Code/PythonCoder/StudentCoder"
        # print(path)
        path_lst = self.path_generate(path)
        self.read_to_save(path_lst)
        # print(path_lst[1])
        # datamanager = DataManager(path_lst[1])
        # datamanager = DataManager(path_lst)
        # datamanager.postfix()
        # print(datamanager.empty_content)


if __name__ == '__main__':
    ss = SimpleSearch()
    ss.main()
