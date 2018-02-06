__author__ = 'LX'
# -*- coding: UTF-8 -*-
# Filename: fingerGuessinGame.py

"""
    这是个猜拳小游戏
"""

import random

while 1:
    s = int(random.randint(1, 3))
    if s == 1:
        ind = '石头'
    elif s == 2:
        ind = '剪刀'
    else:
        ind = '布'
    myGuess = input('请输入 石头、剪刀、布。游戏以end结束：')
    fingerGuessinList = ['石头', '剪刀', '布']
    if (myGuess not in fingerGuessinList) and (myGuess != 'end'):
        print('输入的不合法，请重新输入 石头、剪刀、布。游戏以end结束：')
    elif (myGuess not in fingerGuessinList) and (myGuess == 'end'):
        print('游戏结束！！！')
        break
    elif myGuess == ind:
        print('电脑出了"%s"，平局' % ind)
    elif (ind == '石头' and myGuess == '剪刀') or (ind == '剪刀' and myGuess == '布') or (ind == '布' and myGuess == '石头'):
        print('电脑出了"%s"，电脑赢了' % ind)
    else:
        print('电脑出了"%s"，恭喜您赢了' % ind)

