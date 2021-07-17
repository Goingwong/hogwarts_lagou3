# 1.理解闭包函数的定义
# 2.理解闭包函数的调用
# 3.变量在不同函数中的作用域



# 闭包函数
# 函数定义
name = "鲸鱼"
def func1():
    print("我是func1")
    print(name)
    def func2():
        name = "虾米"
        print("我是func2")
        print(name)

    # 返回 “肚子”里面的函数对象
    return func2

# 不加括号叫函数对象
# func1
# 加括号叫函数的调用
# func1的调用，其实== func2
func22 = func1()
# func22是 return的func2的函数对象
func22()