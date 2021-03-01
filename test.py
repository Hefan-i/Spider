# def fllow(n):
#     return n
# print(fllow(3))
#
# class student(object):
#     def speak(self):
#         print('我的名字是{},我的年龄{}'.format(self.name,self.age))
# hefan=student()
# hefan.name='何帆'
# hefan.age=18
# hefan.speak()


class student(object):
    # 定义构造方法
    def __init__(self, n, a):
        # 设置属性
        self.name = n
        self.age = a

    # 输出一个字符串(追踪对象属性信息变化)
    def __str__(self):  # __str__(self)不可以添加参数(形参)
        return "名字：%s 年龄：%d" % (self.name, self.age)


# 实例化一个对象john
john = student("约翰", 19)

# 当使用print输出对象时，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
print(john)