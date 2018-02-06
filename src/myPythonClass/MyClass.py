__author__ = 'LX'

class MyClass:
    def __init__(self,realpart,imagpart):
        self.r = realpart
        self.i = imagpart

    def f(self):
        return 'hello world'


# 实例化类
x = MyClass(3.9,23)
print(x.i)
print(x.r)