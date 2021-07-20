# 实现被装饰函数有参数的情况
import time

def time_1(time_2):  # 最外层管理 装饰器的参数
    def func1(xxxx): # 管理传入的函数对象
        # 不定长参数，arg代表一个元组，通过位置参数传参；kwargs代表字典，通过关键字传参
        def func2(*args, **kwargs): # 最内层管理 被装饰函数的参数
            if time_2:
                print("开始的时间是", time.strftime("%S"))
                xxxx(args[0])
                print("结束的时间是", time.strftime("%S"))
            else:
                xxxx(args[0])
        return func2
    return func1


# @time_1(time_2 = True)
def be_decorate(m_time):
    time.sleep(m_time)
    print("被装饰器装饰的函数")

# be_decorate(3)


# 拆解装饰器思路
f1 = time_1(time_2 = True)  # 返回func1函数对象
f2 = f1(be_decorate)  # 相当于func1() == 返回func2的函数对象
f2(3)  # 相当于func2()