# Insert your code here.
from aiycwordcloud import aiycwordcloud
import os, webbrowser


class Simple_NlP():

    def __init__(self, path):
        self.path = path

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

    def open_html(self, filename="wordcloud_diamond.html"):
        r = os.getcwd() + "/" + filename  # /Users/huangjiabao/GitHub/python-library/aiycsnlp/tests
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
        filename = "demo.html"
        aiycwordcloud(words=words, filename=filename, title="demo")
        self.open_html(filename)


if __name__ == '__main__':
    path = "data-test/I_have_a_Dream.txt"
    opt = Simple_NlP(path=path)
    opt.main()
