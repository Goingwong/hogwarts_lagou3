# 面向对象
class House():
    # 静态属性 -> 变量
    # 类变量：在类之中、方法之外
    door = "red"
    floor = "white"

    # 构造函数：在类实例化的时候直接执行
    def __init__(self):
        # 实例变量：类体中，方法内，以self.变量名 的方式来定义
        # 实例变量的作用域：这个类中的所有方法
        print(self.door)
        self.yangtai = "大"

    # 动态属性 -> 方法（函数）
    def sleep(self):
        print(self.yangtai)
        # 普通变量：在类的方法之中，并且不会以 self.
        self.shuijiao = "房子是用来睡觉的"

    def cook(self):
        print(self.yangtai)
        print(self.shuijiao)
        print("房子可以做饭吃")

north = House()
north.sleep()
north.cook()




# # 实例化 -> 变量 = 类()
# north_house = House()
# china_house = House()
#
# # 调用类变量
# print(House.door)
# House.door = "white"
#
# north_house.door = "black"
# print(north_house.door)
#
# print(House.door)
# print(china_house.door)