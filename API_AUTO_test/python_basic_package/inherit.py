class RobotOne:  # 第一代机器人
    def __init__(self, year, name):
        self.year = year
        self.name = name

    def walking_on_ground(self):
        print(self.name + "只能在平地上行走，有障碍物就会摔倒")

    def robot_info(self):
        print("{0}年生产的机器人{1}，是中国研发的".format(self.year, self.name))


class RobotTwo():
    def __init__(self, name):
        self.name = name

    def walking_on_ground(self):
        print(self.name + "可以在平地上行走")

    def walking_avoid_block(self):
        self.robot_info()
        print(self.name + "可以避开障碍物")


class RobotThree(RobotTwo, RobotOne):
    def jump(self):
        print(self.name + "可以单膝跳跃")


r3 = RobotThree("大王")
r3.jump()
r3.walking_on_ground()
r3.robot_info()

# t = RobotTwo("1990", "小王")
# t.robot_info()
# t.walking_on_ground()
# t.walking_avoid_block()

# r1 = RobotOne("1988", "小明")
# r1.walking_on_ground()

# 多继承
# 具有两个父类的属性和方法，如果两个父类有同名方法的时候，就近原则

#超继承
# super(MathMethod_1,self).add()