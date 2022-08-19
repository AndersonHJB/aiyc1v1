class Q1():
    def __init__(self):
        self.question = "题目\n" \
                        "设计一个类 Person，生成若干实例，在终端输出如下信息\n" \
                        "小明，10岁，男，上山去砍柴\n" \
                        "小明，10岁，男，开车去东北\n" \
                        "小明，10岁，男，最爱大保健\n" \
                        "老李，90岁，男，上山去砍柴\n" \
                        "老李，90岁，男，开车去东北\n" \
                        "老李，90岁，男，最爱大保健\n" \
                        "答案获取代码:"

    def get_question(self):
        print(self.question)
        return self.question


class Q1Answer():
    # 构造方法，为实例对象初始化属性
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    # 获取对象属性的方法
    def GetSelfMessage(self):
        return self.name, self.age, self.sex

    # 实例方法，用于实例对象执行某种行为
    def DoSomething(self, doing):
        print(*self.GetSelfMessage(), doing)


if __name__ == '__main__':
    q = Q1().get_question()
