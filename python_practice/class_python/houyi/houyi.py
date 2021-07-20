from python_practice.class_python.game.game import Game

# 快捷键导入，鼠标放到类名处，alt+回车
class HouYi(Game):
    # 如果重名的话，子类的属性会覆盖掉父类的属性
    def __init__(self):
        self.defense = 100
        # 继承父类的构造方法，如果父类的构造方法有形参，需要传递参数
        super().__init__(1000,1300)

    def fight(self):
        while True:
            self.my_hp = self.my_hp + self.defense - self.your_power
            self.your_hp = self.your_hp - self.my_power
            print(self.my_hp)
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.your_hp <= 0:
                print("你输了")
                break