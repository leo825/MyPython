__author__ = 'LX'

# -*- coding: UTF-8 -*-
# Filename:basicGrammar.py

import time

x = 'adfasd';
y = '12312';
print(x),
print(y),

var1 = 1


str = 'hello world!'
print(str)

print(str[0])
print(str[2:5])
print(str[2:])
print(str *2)
print(str + "TESSYT")

print('-------list---------')
list = ['runoob',768,2.23,'john',70.2]
tinylist = [123,'john']

print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist *2)
print(list + tinylist)


print('-------tuple--------')
tuple = ('runoob','768',2.23,'john',70.2)

tinytuple = (123,'john')

print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple *2)
print(tuple + tinytuple)

print('------------dict----------')
dict2 = {}
dict2['one'] = 'This is one'
dict2[2] = 'this is two'

print(dict2)
print(dict2['one'])
print(dict2[2])

test1='1'
print(int(test1))

print('----------python算数运算符------------')
a = 21
b = 10
print('%d + %d = %d' % (a,b,a+b))
print('%d - %d = %d' % (a,b,a-b))
print('%d * %d = %d' % (a,b,a-b))
print('%d / %d = %d' % (a,b,a/b))
print('%d %% 2 = %d' % (a,a%2))#这个是对a求余数，注意百分号的转译
print('%d ** 2 = %d' % (a,a**2))#这个是求幂
print('%d // 2 = %d' % (a,a//2))#这个是求整

print(a,'+',b,'=',a+b) #这只是说明另一种输出的方式


print('---------------if条件句----------------')
score = 100
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('一般')
elif score >= 60:
    print('及格')
else:
    print('不及格')


print('---------while----------')
numbers = [12,37,5,42,8,3]
even = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if(number % 2 == 0):
        even.append(number)
    else:
        odd.append(number)
else: # while...else 循环
    print('while循环结束了')
print(numbers)
print(even)
print(odd)

print('------------for--------------')
for n in range(2,10):
    for x in range(2,n):
        if(n%x == 0):
            print(n,'等于',x,'*',n//x)
            break
    else:
        #循环中没有找到元素
        print(n,'是质数')

print('------------9*9乘法表--------------')
# 外边一层循环控制行数
# i是行数
i=1
while i<=9:
    #里面一层循环控制每一行中的列数
    j=1
    while j<=i:
        mut =j*i
        print('%d*%d=%d'%(j,i,mut), end=" ")
        j+=1
    print("")
    i+=1


print('----------迭代器--------------')
list = [1,2,3,4]
it = iter(list)
for it_temp in it:
    print(it_temp, end=" ")
print()

print('----------生成器--------------')

def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while counter < n:
        yield a
        a, b = b, a + b
        #print(a)
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成

for f_temp in f:
    print(f_temp,end=' ')
print()



print('-----------------函数--------------------')
def hello():
    print('Hello world,I am a method!')
hello()

# 计算长方形面积方法
def area(width,height):
    return width*height

"""
    可更改(mutable)与不可更改(immutable)对象

    在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。
    不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。
    可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

    不可变对象传递过程中不影响当前变量，而可变对象传递过程中会影响当前对象的值

    python 函数的参数传递：
    不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
    可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响

    python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

"""
# 传不可变对象实例
def changeInt(a):
    a = 10
b = 2
changeInt(b)
print(b)

# 传可变对象实例
def changeMe(list):
    list.append([1,2,3,4])
    print('函数内取值：',list)
    return
mylist = [10,20,30]
changeMe(mylist)
print('函数外取值：',mylist)


# 方法中可以设置默认参数
def printinfo(name,age=35):
    print('名字：',name)
    print('年龄',age)
    return
printinfo('runoob',12)

# 不定长参数
def printinfo(arg1,*vartuple):
    print('输出：')
    print(arg1)
    for i in vartuple:
        print(i)
    return

printinfo(10)
printinfo(70,80,90)


#python 使用lambda来创建匿名函数
"""
    所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
    lambda 只是一个表达式，函数体比 def 简单很多。
    lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
    lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
    虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
"""

sum = lambda arg1,arg2:arg1+arg2;
print('相加后的值为:',sum(10,20))


"""
    变量作用域
    Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
    变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
    L （Local） 局部作用域
    E （Enclosing） 闭包函数外的函数中
    G （Global） 全局作用域
    B （Built-in） 内建作用域
    以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。
"""
x = int(2.9)  # 内建作用域

g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域


"""
    global 和 nonlocal关键字
    当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
"""

num =1
def fun1():
    global num # 需要使用global关键字声明
    print(num)
    num = 123
    print(num)

fun1()


# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了，如下实例：
def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
outer()


print('--------------模块--------------')




print('------------time-------------')
localtime = time.localtime(time.time())

print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


print('-------------------http----------------------')
from urllib.request import urlopen
from urllib.parse import quote
reqUrl = 'http://www.sojson.com/open/api/weather/json.shtml?city=北京'
print(quote(reqUrl,safe='/:?=&'))
for line in urlopen(quote(reqUrl,safe='/:?=&')):
    line = line.decode('utf-8')
    print(line)

print('---------------------IO---------------------------')
# 写文件
with open('test.txt','wt',encoding='utf8') as out_file:
    out_file.write('该文本会写入到文件中\n看到我了吧!!!!!!!!!!!!')

# 读文件
with open('test.txt','rt',encoding='utf8') as in_file:
    text = in_file.read()
    print(text)





