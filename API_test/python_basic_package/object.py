class BoyFriend:
    #类属性
    height = 175
    weight = 130
    money = "500w"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    #类函数
    def coding(self, line, language = 'python'):
        print(self.name + "会敲{0}代码,写了{1}行".format(language, line))
    def cooking(self, *args):
        for item in args:
            print("男朋友要会做饭{0}".format(item))

    def earn(self):
        print("男朋友月薪是3万")

    @classmethod
    def swiming(cls):
        print("游泳")

    @staticmethod
    def sing():
        print("唱歌")


bf = BoyFriend()
BoyFriend.cooking(bf)
bf.cooking()

bf = BoyFriend("花花", "18")

# 类里面的方法分为三种：
#实例方法self：意味着这个方法只能实例来调用
#类方法cls
#静态方法
#实例和类名都可以调用
#静态方法和类方法不可以调用类里面的属性值