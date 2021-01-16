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

# 4 break contiue 
# break 用来终止循环 用在while和for循环中 直接跳出整个循环
# continue 是跳出当前循环

# 3 assert 
# 声明其布尔值必须为真的判定 如果发生异常就说明表达示为假
# assert 1 == 2  # AssertionError
# assert 1 == 1

# 2 and or
# and 和 or 逻辑关系用语
# False and 返回 False 不执行后面的语句
# True or 直接返回True，不执行后面的语句 

# 1 False True None
# 前两个是bool值 不用多说  None 属于特殊类型
# print(None, type(None))  # None <class 'NoneType'>
