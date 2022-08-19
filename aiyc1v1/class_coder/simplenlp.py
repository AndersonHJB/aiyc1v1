# Insert your code here.
import os, webbrowser
from aiyc1v1.class_coder.wordcloud import wordcloud


class Simple_NlP():
    def __init__(self, path, filename="wordcloud_diamond.html", auto_open=True):
        self.path = path
        self.filename = filename
        self.auto_open = auto_open

    def read(self, path):
        with open(path, "r", encoding="utf-8") as f:
            return f.readlines()

    def rinse(self, contents):
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
        no_have_words = [
            "no", "am", "the", "The", "an",
            "I", "a", "of", "to", "and", "be",
            "that",
        ]
        for nh in no_have_words:
            if nh in word_dict:
                del word_dict[nh]
            else:
                pass
        # print(word_dict)
        return word_dict

    def open_html(self):
        r = os.getcwd() + "/" + self.filename  # /Users/huangjiabao/GitHub/python-library/aiycsnlp/tests
        webbrowser.open('file:///' + r)

    def main(self):
        contents = self.read(self.path)
        # print(contents)
        rinse = self.rinse(contents)
        # print(rinse)
        word_dict = self.parse(rinse)
        cw = self.clear_no_have(word_dict)
        words = list(cw.items())
        print(words)
        # filename = "demo.html"
        wordcloud(words=words, filename=self.filename, title="demo")
        if self.auto_open:
            self.open_html()


if __name__ == '__main__':
    path = "data-test/I_have_a_Dream.txt"
    opt = Simple_NlP(path=path)
    opt.main()
