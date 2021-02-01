#导入keyword 模块
import keyword
#显示所有关键字
# print(keyword.kwlist)

"""python 3.6 版本
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""

# 21 yield
# 任何使用yield的函数都称之为生成器 而生成器通常可理解成迭代器
# 迭代器 yield的意思是生产 返回了一个生成器对象 每个生成器只能使用一次
# def cou(n):
#     while n>0:
#         yield n
#         n -= 1
# c = cou(3)
# print(c.__next__())  # 3
# print(next(c))  # 2
# print(next(c))  # 1
# print(next(c))  # StopIteration

# 20 with
# 后面返回的对象要求必须两__enter__()/__exit__()这两个方法
# 需要事先做一些设置 事后做一些清理
# class Test:
#     def __enter__(self):
#         print('__enter__() is call!')
#         return self

#     def dosomething(self):
#         x = 1/0
#         print('dosomethong!')

#     def __exit__(self, exc_type, exc_value, traceback):
#         print('__exit__() is call!')
#         print(f'type:{exc_type}')
#         print(f'value:{exc_value}')
#         print(f'trace:{traceback}')
#         print('__exit()__ is call!')
#         return True

# with Test() as sample:
#     sample.dosomething()
# # __enter__() is call!
# # __exit__() is call!
# # type:<class 'ZeroDivisionError'>
# # value:division by zero
# # trace:<traceback object at 0x000000000299A548>
# # __exit()__ is call!

# 19 return
# 保留函数最终的值，并终结程序运行

# 18 raise
# 抛出异常
# raise [Exception[,args[,traceback]]] 
# 语句中Exception是异常的类型 例如: NameError 参数是一个异常参数值

# 17 pass
# 占位符

# 16 nonlocal
# 用于标识外部作用域的变量
# 它是用在封装函数中的 且一般使用于嵌套函数的场景中
# 闭包只能读外部函数的变量，而不能改写它
# def a():
#   x = 0
#   def b():
#     print(locals())  # {'x': 0}
#     y = x + 1
#     print(locals())  # {'x': 0, 'y': 1}
#     # x = x + 1  # UnboundLocalError: local variable 'x' referenced before assignment
#     print(x, y)  # 0 1
#   return b
 
# a()()
# ----下面是 nonlocal 的用法
# def a():
#   x = 0
#   def b():
#     print(locals())  # {'x': 0}
#     y = x + 1
#     print(locals())  # {'x': 0, 'y': 1}
#     print(x, y)  # 0 1
#   return b
# a()()


# 15 lambda
# 匿名函数，此关键字可以用一行实现一个函数

# 14 is
# (1)判断两个变量的指向是否完全一致，及内容与地址需要完全一致，才返回True，否则返回False
# (2)判断变量是否为某个类的实例
# 很特殊的两个例子
# a = 10
# b = 10
# print(a is b)  # True
# a = 10
# def f():
#     return 10
# print(f() is a)  # True
# 第二个 这两个不一样的原因是因为字节码的问题 完全看不懂
# https://github.com/hinus/railgun/blob/master/src/main/python/rgparser/show.py
# a = 10.0
# b = 10.0
# print(a is b)  # True
# a = 10.0
# def f():
#     return 10.0
# print(f() is a)  # False

# 13 global
# 一般在局部或函数内对全局变量进行修改，须在局部用 global 声明变量,不然无法修改
# a = 1
# print(a)  # 1
# def buti(num):
#     print(num)  # 5
#     global a
#     print(a)  # 1
#     a = num
#     print(a)  # 5
# buti(5)
# print(a)  # 5

# 12 import from
# 导包
# from 导包进来的变量容易被覆盖 import 的不会
# from math import pi
# print(pi)
# pi = 666
# print(pi)

# import math
# print(math.pi)

# 11 for in while
# 循环语句

# 10 try except else finally
# 有异常执行 except 没异常执行 else 不管有没有异常执行 finally

# 9 if elif else
# 配合使用
# a = 1
# if a == 1:
#     print(a)
# elif a == 2:
#     print(a)
# else:
#     print(a)

# 8 del
# 删除字典的键
# 或者是删除变了
# a = 1
# print(a)  # 1
# del a
# print(a)  # NameError: name 'a' is not defined

# 7 def
# 用于定义函数

# 6 class
# 只可意会不可言传的东西
# 用于定义类

# 5 as
# 给我的感觉就是重命名
# import numpy as np
# with open('file') as f:
#    pass

# 4 break contiue
# break 用来终止循环 用在while和for循环中 直接跳出整个循环
# continue 是跳出当前循环

# 3 assert
# 声明其布尔值必须为真的判定 如果发生异常就说明表达示为假
# assert 1 == 2  # AssertionError
# assert 1 == 1

# 2 and or not ---> 优先级 not > and > or
# and 和 or 逻辑关系用语
# False and 返回 False 不执行后面的语句
# True or 直接返回True，不执行后面的语句 

# 1 False True None
# 前两个是bool值 不用多说  None 属于特殊类型
# print(None, type(None))  # None <class 'NoneType'>