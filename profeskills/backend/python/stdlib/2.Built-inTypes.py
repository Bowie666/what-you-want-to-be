# 主要内置类型有数字、序列、映射、类、实例和异常。


"""
4. 数字类型 — int, float, complex
存在三种不同的数字类型: 整数, 浮点数 和 复数。 此外，布尔值属于整数的子类型。 整数具有无限的精度。
所有数值类型（复杂类型除外）都支持按升序优先级排序的以下操作（所有数值操作的优先级都高于比较操作）："""


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
object.__eq__(self, other)¶
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