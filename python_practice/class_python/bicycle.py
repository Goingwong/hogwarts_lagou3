

class Bicycle:
    def run(self,km):
        print(f"一共用脚骑行{km}公里，累死了")

# bike = Bicycle()
# bike.run(20)

# 继承类
class EBicycle(Bicycle):
    # 如果属性需要传参定义，那么可以使用构造函数
    def __init__(self,valume):
       self.valume = valume
    def fill_charge(self,vol):
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量为{self.valume}")
    def run(self,km):
        # 获得目前电量所能电动骑行的最大里程数
        power_km = self.valume*10
        #如果电量所能支持骑行的最大里程>要骑行的里程，全程用电骑行足够
        if power_km >= km:
            print(f"我使用电瓶电量骑了{km}公里")
        else:
            print(f"我已经使用电瓶骑行了{power_km}公里")
            # 非继承调用
            # bike = Bicycle()
            # bike.run(km - power_km)
            # 继承调用
            super().run(km - power_km)

        print()

ebike = EBicycle(10)
# ebike.fill_charge(3)
ebike.run(150)