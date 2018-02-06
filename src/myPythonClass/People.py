__author__ = 'LX'

# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性，私有属性外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print('%s 说：我 %d岁了。' %(self.name,self.age))

# 单继承示例，学生类
class Student(People):
    grade = ''
    def __init__(self,n,a,w,g):
        # 调用父类的构造方法
        People.__init__(self,n,a,w)
        self.grade = g
    # 覆盖父类的方法
    def speak(self):
        print('%s 说：我%d岁了，我在读%d年级' %(self.name,self.age,self.grade))


# 演讲类
class Speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print('我叫%s，我是一个演说家，我演讲的主题是%s' %(self.name,self.topic))

# 多重继承
class Sample(Speaker,Student):
    a = ''
    def __init__(self,n,a,w,g,t):
        Student.__init__(self,n,a,w,g)
        Speaker.__init__(self,n,t)


test = Sample("Tim",25,80,4,"Python")
test.speak()   # 方法名同，默认调用的是在括号中排前地父类的方法


"""
类的专有方法：
__init__ : 构造函数，在生成对象时调用
__del__ : 析构函数，释放对象时使用
__repr__ : 打印，转换
__setitem__ : 按照索引赋值
__getitem__: 按照索引获取值
__len__: 获得长度
__cmp__: 比较运算
__call__: 函数调用
__add__: 加运算
__sub__: 减运算
__mul__: 乘运算
__div__: 除运算
__mod__: 求余运算
__pow__: 乘方

"""

"""
    运算符重载
    Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：运算符重载
    Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：
"""

class Vector:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return 'Vector (%d,%d)' %(self.a,self.b)
    def __add__(self, other):
        return Vector(self.a+other.a,self.b+other.b)

v1 = Vector(1,3)
v2 = Vector(5,6)
print(v1)

