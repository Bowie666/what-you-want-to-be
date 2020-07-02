# 主要内置类型有数字、序列、映射、类、实例和异常。
"""
5. 迭代器类型
Python 支持在容器中进行迭代的概念。 这是通过使用两个单独方法来实现的；它们被用于允许用户自定义类对迭代的支持。"""
# container.__iter__()  # 返回一个迭代器对象。

# 迭代器对象自身需要支持以下两个方法，它们共同组成了 迭代器协议:

# iterator.__iter__()  # 返回迭代器对象本身。 这是同时允许容器和迭代器配合 for 和 in 语句使用所必须的。
# iterator.__next__()  # 从容器中返回下一项。 如果已经没有项可返回，则会引发 StopIteration 异常。 
# (1) 生成器类型
# Python 的 generator 提供了一种实现迭代器协议的便捷方式。
# 如果容器对象 __iter__() 方法被实现为一个生成器，它将自动返回一个迭代器对象（从技术上说是一个生成器对象）
# 该对象提供 __iter__() 和 __next__() 方法。去看yield

"""
4. 数字类型 — int, float, complex
存在三种不同的数字类型: 整数, 浮点数 和 复数。 此外，布尔值属于整数的子类型。 整数具有无限的精度。
所有数值类型（复杂类型除外）都支持按升序优先级排序的以下操作（所有数值操作的优先级都高于比较操作）："""
# # 1 按位运算就把数字转换为机器语言——二进制的数字来运算的一种运算形式。在计算机系统中，数值一律用补码来表示(存储)。
# a = 10
# b = 6

# print(a|b)  # 14
# print(a^b)  # 12
# print(a&b)  # 2
# print(b>>1)  # 3
# print(b<<1)  # 12
# print(~b)  # -7

# 2 整数类型的附加方法
# (byteorder 参数确定用于表示整数的字节顺序。 
# 如果 byteorder 为 "big"，则最高位字节放在字节数组的开头。 
# 如果 byteorder 为 "little"，则最高位字节放在字节数组的末尾。)

# (1)int.bit_length() 返回以二进制表示一个整数所需要的位数，不包括符号位和前面的零:
# n = -37
# print(bin(n))  # -0b100101
# print(n.bit_length())  # 6

# (2)int.to_bytes(length, byteorder, *, signed=False)返回表示一个整数的字节数组。
# print((1024).to_bytes(2, byteorder='big'))  # b'\x04\x00'
# print((1024).to_bytes(10, byteorder='big'))  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'
# print((-1024).to_bytes(10, byteorder='big', signed=True))  # b'\xff\xff\xff\xff\xff\xff\xff\xff\xfc\x00'
# x = 1000
# print(x.to_bytes((x.bit_length() + 7) // 8, byteorder='little'))  # b'\xe8\x03'

# (3)int.from_bytes(bytes, byteorder, *, signed=False)返回由给定字节数组所表示的整数。
# print(int.from_bytes(b'\x00\x10', byteorder='big'))  # 16
# print(int.from_bytes(b'\x00\x10', byteorder='little'))  # 4096
# print(int.from_bytes(b'\xfc\x00', byteorder='big', signed=True))  # -1024
# print(int.from_bytes(b'\xfc\x00', byteorder='big', signed=False))  # 64512
# print(int.from_bytes([255, 0, 0], byteorder='big'))  # 16711680

# 3 浮点类型的附加方法
# (1)float.as_integer_ratio() 返回一对整数，其比率正好等于原浮点数并且分母为正数。
# print((10.5).as_integer_ratio())  # (21, 2)
# print((8.3).as_integer_ratio())  # (2336242306698445, 281474976710656)
# print((0.5).as_integer_ratio())
# (2)float.is_integer() 如果 float 实例可用有限位整数表示则返回 True，否则返回 False:
# print((-2.0).is_integer())  # True
# print((3.2).is_integer())  # False
# (3)float.hex() 以十六进制字符串的形式返回一个浮点数表示。是实例方法
# print(float.fromhex('0x3.a7p10'))  # 3740.0
# (4)float.fromhex(s) 返回以十六进制字符串 s 表示的浮点数的类方法。
# print(float.hex(3740.0))  # 0x1.d380000000000p+11

# 4.4.4. 数字类型的哈希运算
# 有点迷糊 没看懂
# 哈希的定义是：简单的说就是一种将任意长度的消息压缩到某一固定长度的消息摘要的函数。
# print(hash("123"))  # 8666272638186902008
# 这part主要阐述int float complex fraction的hash制定规则

"""
3. 比较运算
在 Python 中有八种比较运算符。 它们的优先级相同（比布尔运算的优先级高）。 
比较运算可以任意串连；例如，x < y <= z 等价于 x < y and y <= z，
前者的不同之处在于 y 只被求值一次（但在两种情况下当 x < y 结果为假值时 z 都不会被求值）。

此表格汇总了比较运算:

运算    含义

<       严格小于
<=      小于或等于
>       严格大于
>=      大于或等于
==      等于
!=      不等于
is      对象标识
is not  否定的对象标识

还有两种具有相同语法优先级的运算 in 和 not in，它们被 iterable 或实现了 __contains__() 方法的类型所支持。

补充：
object.__lt__(self, other)
object.__le__(self, other)
object.__eq__(self, other)
object.__ne__(self, other)
object.__gt__(self, other)
object.__ge__(self, other)
以上这些被称为“富比较”方法。
运算符号与方法名称的对应关系如下：
x<y 调用 x.__lt__(y)、
x<=y 调用 x.__le__(y)、
x==y 调用 x.__eq__(y)、
x!=y 调用 x.__ne__(y)、
x>y 调用 x.__gt__(y)、
x>=y 调用 x.__ge__(y)。
"""

"""
2. Boolean Operations — and, or, not
这些属于布尔运算，按优先级升序排列:

运算        结果：                                      注释

x or y      if x is false, then y, else x              这是个短路运算符，因此只有在第一个参数为假值时才会对第二个参数求值
x and y     if x is false, then x, else y              这是个短路运算符，因此只有在第一个参数为真值时才会对第二个参数求值。
not x       if x is false, then True, else False       not 的优先级比非布尔运算符低，因此 not a == b 会被解读为 not (a == b) 而 a == not b 会引发语法错误。

"""

"""
1. 逻辑值检测
下面基本完整地列出了会被视为假值的内置对象

被定义为假值的常量: None 和 False。
任何数值类型的零: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
空的序列和多项集: '', (), [], {}, set(), range(0)
"""