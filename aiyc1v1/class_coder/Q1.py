class Q1():
    def __init__(self):
        self.question = """题目\n设计一个类 Person，生成若干实例，在终端输出如下信息\n小明，10岁，男，上山去砍柴\n小明，10岁，男，开车去东北\n小明，10岁，男，最爱大保健\n老李，90岁，男，上山去砍柴\n老李，90岁，男，开车去东北\n老李，90岁，男，最爱大保健"""

    def get_question(self):
        print(self.question)


if __name__ == '__main__':
    q = Q1().get_question()
