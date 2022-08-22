# Insert your code here.
import os, webbrowser
from aiyc1v1.class_coder.wordcloud import wordcloud


class Simple_NlP():
    """
    NLP 基本词频分析
    """

    def __init__(self, path: str, clear_words: list, clear_symbols: list, filename="defualt.html", auto_open=True):
        """
        :param
            path: str, operation file path.
            filename: output html file, defualt name.
            auto_open: 是否自动打开生成的词云文件，默认为 True
            clear_words: 清除无意义的单词，列表传入
            clear_symbols: 具体功能待实现
        :return:
        """
        self.path = path
        self.filename = filename
        self.auto_open = auto_open
        self.clear_words = clear_words
        self.clear_symbols = clear_symbols

    def read(self, path):
        """
        :param
            path: str, operation file path.
        :return:
        """
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()

    def rinse(self, contents):
        """
        :param
            contents: str, 清洗不需要的符号
        :return: lst: list
        """
        lst = []
        for lines in contents:
            lines = lines.replace(",", "")
            lines = lines.replace("?", "")
            lines = lines.replace("'", "")
            # lines = lines.replace("'", "")
            lines = lines.replace("\n", "")
            lines = lines.replace(".", "")
            lines = lines.replace("-", "")
            lines = lines.replace(":", "")
            lines = lines.replace(".", "")
            lines = lines.replace("/", " ")
            lines = lines.replace("—", "")
            lines = lines.replace("—", "")
            # print(lines, end="")
            # ""
            if lines:
                lst.append(lines)
        return lst

    def parse(self, rinse):
        # word_count = []
        # n = 0
        word_dict = {}
        for line in rinse:
            word_lst = line.split(" ")
            # print(len(word_lst))
            # n += len(set(word_lst))
            for word in word_lst:
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1
        # print(word_dict)
        return word_dict

    def clear_no_have(self, word_dict):
        """清除无意义的的单词"""
        # no_have_words = [
        #     "no", "am", "the", "The", "an",
        #     "I", "a", "of", "to", "and", "be",
        #     "that",
        # ]
        for nh in self.clear_words:
            if nh in word_dict:
                del word_dict[nh]
            else:
                pass
        # print(word_dict)
        return word_dict

    def open_html(self, filename: str):
        r = os.getcwd() + "/" + filename  # /Users/huangjiabao/GitHub/python-library/aiycsnlp/tests
        webbrowser.open('file:///' + r)

    def main(self):
        contents = self.read(self.path)
        # print(contents)
        rinse = self.rinse(contents)
        # print(rinse)
        word_dict = self.parse(rinse)
        cw = self.clear_no_have(word_dict)
        words = list(word_dict.items())
        print(words)
        # filename = "demo.html"
        wordcloud(words=words, filename=self.filename, title="demo")
        if self.auto_open:
            self.open_html(self.filename)


if __name__ == '__main__':
    path = "data-test/I_have_a_Dream.txt"
    opt = Simple_NlP(path=path)
    opt.main()
