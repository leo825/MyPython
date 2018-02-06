__author__ = 'LX'
# -*- coding: UTF-8 -*-


"""
    这个小游戏是输入数字然后猜数字是多少
"""

number = 7
guess = -1
while guess != number:
    guess = int(input('请输入数字: '))
    if guess == number:
        print('恭喜，你猜对了！')
        break
    elif guess < number:
        print('猜的数字小了。。。')
    elif guess > number:
        print('猜的数字大了。。。')


from myPythons import BasicGrammar

f = BasicGrammar.fibonacci(10) # f 是一个迭代器，由生成器返回生成

for f_temp in f:
    print(f_temp,end=' ')
print()
