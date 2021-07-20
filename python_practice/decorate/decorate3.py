# 实现被装饰函数有参数的情况
import time


def func1(xxxx):
    def func2(m_time):
        print("开始的时间是", time.strftime("%S"))

        xxxx(m_time)

        print("结束的时间是", time.strftime("%S"))
    return func2


@func1
def be_decorate(m_time):
    time.sleep(m_time)
    print("被装饰器装饰的函数")


@func1
def demo2():
    time.sleep(4)
    print("这是一个小demo")



be_decorate(3)