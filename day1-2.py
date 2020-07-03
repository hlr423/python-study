# -*- coding: utf-8 -*-
# print('======gaogao========')
# a=input('高高在干嘛：')
# b=int(a)
# if b==8:
#     print('gaogao教我写python')
#     print('我猜对了吗？')
# else:
#     print('对不起！你猜错了，高高在看电视剧')
# print('game over！')
#
# BIF ==built-in function 是 内 置 函 数
# 赋值变量
# teacher = '小高'
# print(teacher)
# teacher='老高'
# print(teacher)
#
# 拼接
# a='yuang gao'
# b='old gao'
# c=a+b
# print(c) yuang gaoold gao
#
# c=5+8
# 13
# c='5'+'8'
# 58 58是字符串，这是5和8的字符串的拼接
#
# 变量的命名可以是任意，见名知义即可
# 转义字符
# str = 'let's go'
# 1、报错，' 必须要转译
# str = 'let\'s go'
# 2、"let's go"
#
# 对一个字符串中有很多个反斜杠时，可以使用原始字符串的处理方法，只需要在字符串前面加一个英文字母 r 即可
# str=r'c:\new\file\text.js'  # 'c:\\new\\file\\text.js'
# print(str)
# c:\new\file\text.js
# '''表示注释
# 实例如下：
# '''
# ... dddd
# ... ddd
# ... ddd
# ... ddd
# ... '''
# '\ndddd\nddd\nddd\nddd\n'


# while 嵌套if else 使用    and为有true为true，or为 true true为true
# temp=input('输入number：')
# num=int(temp)
# i=1
# while num !=8 and i<4:
#     if num==8:
#         print("恭喜你答对了")
#     else:
#         if num>8:
#             print("对不起！你输入的数字太大了")
#         else:
#             print("对不起！你输入的数字太小了")
#     temp=input('请重新输入吧')
#     num=int(temp)
#     i=i+1
# print("游戏结束，不玩了")

# 完善的小游戏代码：
# i = 1
# print(type(i))
# while i < 4:
#     temp = input('输入number：')
#     num = int(temp)
#     if num == 8:
#         print("恭喜你答对了")
#         break
#     else:
#         if num > 8:
#             print("对不起！你输入的数字太大了")
#         else:
#             print("对不起！你输入的数字太小了")
#         i = i+1
# print("游戏结束，不玩了")

# python 的数据类型有哪些？
# 整型、布尔类型、浮点类型 、e记法
# int()、str()、float()

# a = '520'
# b = int(a)
# c = 5.22
# print(int(c))     # 浮点转换成整型直接保留整数去掉小数位 5
# print(float(b))   # 浮点转换成整型直接保留整数去掉小数位  520.0
# d = 5.99
# print(str(d))     # 浮点转换成整型直接保留整数去掉小数位  '5.99'
# print(str(5e19))  # 5e+19   5的19次方
# print(b)    # '520'

# python中的关键字 str():将数据转换成字符串

# str = 'i love you'
# print(str)   # ' i love you'
# print(str(5e2))     # 报错：TypeError: 'str' object is not callable
# 原因:当str被赋值为一个字符串时，它没有callable，就变成了一个变量名，不在是python内置方法，str就不能做数据类型转换了，因此报错了

# type()函数，查看数据类型    isinstance() 判断两个参数的类型，true为类型相同，false为类型不同
# a = type(1)     # <class 'int'>
# b = isinstance(3.3, float)   # True
# c = isinstance(3, float)   # False
# d = isinstance('a', str)   # True
# e = isinstance('true', float)   # True
# print(a, c, d)