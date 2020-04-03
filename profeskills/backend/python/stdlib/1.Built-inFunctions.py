"""23 format(value[, format_spec])
将 value 转换为 format_spec 控制的“格式化”表示。
format_spec 的解释取决于 value 实参的类型，但是大多数内置类型使用标准格式化语法：格式规格迷你语言。
默认的 format_spec 是一个空字符串，它通常和调用 str(value) 的结果相同。"""
print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
print("{0} {1}".format("hello", "world"))  # 设置指定位置
print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))

site = {"name": "菜鸟教程", "url": "www.runoob.com"}  # 通过字典设置参数
print("网站名：{name}, 地址 {url}".format(**site))

my_list = ['菜鸟教程', 'www.runoob.com']  # 通过列表索引设置参数
print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

"""22 class float([x])  返回浮点数
返回从 数字 或 字符串 x 生成的浮点数。
如果实参是字符串，则它必须是包含十进制数字的字符串，字符串前面可以有符号，之前也可以有空格。
可选的符号有 '+' 和 '-' ； '+' 对创建的值没有影响。实参也可以是 NaN（非数字）、正负无穷大的字符串。"""
# print(float('+1.23'))  # 1.23
# print(float('   -12345\n'))  # -12345.0
# print(float('1e-003'))  # 0.001
# print(float('+1E6'))  # 1000000.0
# print(float('-Infinity'))  # -inf

"""21 filter(function, iterable) 第一个是函数，第二个是一个可迭代的序列
用 iterable 中函数 function 返回真的那些元素，构建一个新的迭代器。
iterable 可以是一个序列，一个支持迭代的容器，或一个迭代器。
如果 function 是 None ，则会假设它是一个身份函数，即 iterable 中所有返回假的元素会被移除。
filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，如果要转换为列表，可以使用 list() 来转换。"""
# def is_odd(n):
#     return n % 2 == 1
# print(filter(is_odd, [1, 2, 3, 4, 5]))  # <filter object at 0x0000000009D520F0>
# print(type(filter(is_odd, [1, 2, 3, 4, 5])))  # <class 'filter'>
# print(list(filter(is_odd, [1, 2, 3, 4, 5])))  # [1, 3, 5]
# print(filter(is_odd, (1, 2, 3, 4, 5)))  # <filter object at 0x0000000009D520F0>
# print(type(filter(is_odd, (1, 2, 3, 4, 5))))  # <class 'filter'>
# print(list(filter(is_odd, (1, 2, 3, 4, 5))))  # [1, 3, 5]
# print(tuple(filter(is_odd, (1, 2, 3, 4, 5))))  # (1, 3, 5)

"""20 exec(object[, globals[, locals]])
这个函数支持动态执行 Python 代码。object 必须是字符串或者代码对象。
如果是字符串，那么该字符串将被解析为一系列 Python 语句并执行（除非发生语法错误）。
如果是代码对象，它将被直接执行。在任何情况下，被执行的代码都需要和文件输入一样是有效的。
请注意即使在传递给 exec() 函数的代码的上下文中，return 和 yield 语句也不能在函数定义之外使用。该函数返回值是 None 。
exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。"""
# exec("print('hello')")  # hello
# exec("for i in range(5):print(i)")  # 0\n 1\n 2\n 3\n 4\n

"""19 eval(expression, globals=None, locals=None)
其实这个函数很熟悉了，后期要了解更高级的功能
实参是一个字符串，以及可选的 globals 和 locals。
globals 实参必须是一个字典。
locals 可以是任何映射对象。"""

"""18 enumerate(iterable, start=0)
返回一个枚举对象。
iterable 必须是一个序列，或 iterator，或其他支持迭代的对象。
enumerate() 返回的迭代器的 __next__() 方法返回一个元组，
里面包含一个计数值（从 start 开始，默认为 0）和通过迭代 iterable 获得的值。"""
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(enumerate(seasons))  # <enumerate object at 0x0000000001E06EA0>
# print(list(enumerate(seasons)))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
# print(list(enumerate(seasons, start=1)))  # [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
# 下面这是等价
# def monk(sequence, start=0):
#     n = start
#     for elem in sequence:
#         yield n, elem
#         n += 1
# seasons = ['Spring', 'Summer', 'Fall', 'Winter']
# print(list(monk(seasons)))  # [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]

"""17 divmod(a, b)  就是a除以b
它将两个（非复数）数字作为实参，并在执行整数除法时返回一对商和余数。
对于混合操作数类型，适用双目算术运算符的规则。
对于整数，结果和 (a // b, a % b) 一致。
对于浮点数，结果是 (q, a % b) ，q 通常是 math.floor(a / b) 但可能会比 1 小。
在任何情况下， q * b + a % b 和 a 基本相等；
如果 a % b 非零，它的符号和 b 一样，并且 0 <= abs(a % b) < abs(b) 。"""
# print(divmod(10, 5))  # (2, 0)
# print(divmod(5, 3))  # (1, 2)
# print(divmod(3, 6))  # (0, 3)
# print(divmod(10.8, 5.6))  # (1.0, 5.200000000000001)
# print(divmod(5.3, 3.5))  # (1.0, 1.7999999999999998)
# print(divmod(3.7, 6.5))  # (0.0, 3.7)
# print(divmod(0, 5))  # (0, 0)
# # print(divmod(10, 0))  # ZeroDivisionError: integer division or modulo by zero

"""16 dir([object])
如果没有实参，则返回当前本地作用域中的名称列表。如果有实参，它会尝试返回该对象的有效属性列表。
如果对象有一个名为 __dir__() 的方法，那么该方法将被调用，并且必须返回一个属性列表。
如果对象是模块对象，则列表包含模块的属性名称。
如果对象是类型或类对象，则列表包含它们的属性名称，并且递归查找所有基类的属性。
否则，列表包含对象的属性名称，它的类属性名称，并且递归查找它的类的所有基类的属性。"""
# print(dir())  # ['__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# class Nek():
#     def look(self):
#         return 1
#     def __dir__(self):
#         return 'keyword'
# print(dir(Nek()))  # ['d', 'e', 'k', 'o', 'r', 'w', 'y']

"""15 class dict(**kwarg)：传入关键字参数
class dict(mapping, **kwarg)： 传入映射函数
class dict(iterable, **kwarg)： 传入可迭代对象来构造字典"""
# print(dict())  # {}
# print(dict(a='a', b='b'))  # {'a': 'a', 'b': 'b'}
# print(dict(zip(['o', 'p', 'q'], ['1', '2', '3'])))  # {'o': '1', 'p': '2', 'q': '3'}
# print(dict(zip(['o', 'p', 'q'], ['1', '2', '3'], ['r', 's', 't'],['1', '2','3'])))
# # ValueError: dictionary update sequence element #0 has length 4; 2 is required值错误：字典更新序列元素0的长度为4；需要2
# print(dict(zip(['o', 'p', 'q'], [1, 2, 3])))  # {'o': 1, 'p': 2, 'q': 3}
# print(dict([('one', 1), ('two', 2), ('three', 3)]))  # {'one': 1, 'two': 2, 'three': 3}

"""14 delattr(object, name)
setattr() 相关的函数。实参是一个对象和一个字符串。该字符串必须是对象的某个属性。
如果对象允许，该函数将删除指定的属性。
例如 delattr(x, 'foobar') 等价于 del x.foobar 。"""
# class tet():
#     a = 10
#     b = 20
# c = tet()
# print(c.b)  # 20
# print(c.a)  # 10
# delattr(tet, "a")
# print(c.a)  # AttributeError: 'tet' object has no attribute 'a'

"""13 class complex([real[, imag]])
返回值为 real + imag*1j 的复数，或将字符串或数字转换为复数。
如果第一个形参是字符串，则它被解释为一个复数，并且函数调用时必须没有第二个形参。
第二个形参不能是字符串。每个实参都可以是任意的数值类型（包括复数）。
如果省略了 imag，则默认值为零，构造函数会像 int 和 float 一样进行数值转换。
如果两个实参都省略，则返回 0j。"""
# print(complex("1"))  # (1+0j)
# print(complex(1, 2))  # (1+2j)
# print(complex(1))  # (1+0j)
# print(complex())  # 0j
# print(complex(2, "2"))  # TypeError: complex() second arg can't be a string

"""12 compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)
将 source 编译成代码或 AST 对象。代码对象可以被 exec() 或 eval() 执行。
source 可以是常规的字符串、字节字符串，或者 AST （Abstract Syntax Trees）对象
filename -- 代码文件名称，如果不是从文件读取代码则传递一些可辨认的值（经常会使用 '<string>'）。
mode -- 指定编译代码的种类。可以指定为 exec, eval, single。
flags -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。。
flags和dont_inherit是用来控制编译源码时的标志
Future 语句使用比特位来指定，多个语句可以通过按位或来指定。
    具体特性的比特位可以通过 __future__ 模块中的 _Feature 类的实例的 compiler_flag 属性来获得。
optimize 实参指定编译器的优化级别；默认值 -1 选择与解释器的 -O 选项相同的优化级别。
    显式级别为 0 （没有优化；__debug__ 为真）、1 （断言被删除， __debug__ 为假）或 2 （文档字符串也被删除）。
如果编译的源码不合法，此函数会触发 SyntaxError 异常；如果源码包含 null 字节，则会触发 ValueError 异常。"""
# str1 = "for i in range(0,10): print(i)"
# c = compile(str1, '', 'exec')
# print(c)  # <code object <module> at 0x000000000284A420, file "", line 1>
# print(exec(c))  # 0 1 2 3 4 5 6 7 8 9 None
#
# str2 = "3 * 4 +5"
# a = compile(str2, '', 'eval')
# print(a)  # <code object <module> at 0x00000000028958A0, file "", line 1>
# print(eval(a))  # 17
# print(exec(a))  # None

"""11 @classmethod
把一个方法封装成类方法。就是调用的时候不需要实例化了"""
# a = 666

"""10 chr(i) 就是返回当前整数对应的 ASCII 字符。
返回 Unicode 码位为整数 i 的字符的字符串格式。
例如，chr(97) 返回字符串 'a'，chr(8364) 返回字符串 '€'。这是 ord() 的逆函数。
实参的合法范围是 0 到 1,114,111（16 进制表示是 0x10FFFF）。
如果 i 超过这个范围，会触发 ValueError 异常。"""
# print(chr(41))  # )
# print(chr(97))  # a
# print(chr(8364))  # €

"""9 callable(object)
用于检查一个对象是否是可调用的。如果返回 True，object 仍然可能调用失败；
但如果返回 False，调用对象 object 绝对不会成功。
对于函数、方法、lambda 函式、 类以及实现了 __call__ 方法的类实例, 它都返回 True"""
# print(callable(object))
# print(callable(0))
# print(callable(1))
# print(callable("look"))
# def add(a, b):
#     return a + b
# print(callable(add))
#
# class B:
#     def method(self):
#         return 0
# # 这个是声明
# print(callable(B))
# # 这个是创建实例
# b = B()
# print(callable(b))

"""8 class bytes([source[, encoding[, errors]]])
返回一个新的“bytes”对象， 是一个不可变序列，包含范围为 0 <= x < 256 的整数。
bytes 是 bytearray 的不可变版本 - 它有其中不改变序列的方法和相同的索引、切片操作。"""
# print(bytes())  # b''
# print(bytes(3))  # b'\x00\x00\x00'
# print(bytes(4))  # b'\x00\x00\x00\x00'
# print(bytes([1, 2, 3]))  # b'\x01\x02\x03'
# print(bytes([1, 12, 3, 4]))  # b'\x01\x0c\x03\x04'
# print(bytes('runoob', 'utf-8'))  # b'runoob'

"""7 class bytearray([source[, encoding[, errors]]])
返回一个新的 bytes 数组。 bytearray 类是一个可变序列，包含范围为 0 <= x < 256 的整数。
它有可变序列大部分常见的方法，见 可变序列类型 的描述；同时有 bytes 类型的大部分方法，
x	        创建 bytearray 对象时使用的资源 如果是整数，则会创建指定大小的空 bytearray 对象。
            如果是字符串，请确保规定了资源的编码。
encoding	字符串的编码
error	    规定若编码失败要做什么。

如果 source 为整数，则返回一个长度为 source 的初始化数组；
如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
如果 source 为可迭代类型，则元素必须为[0 ,255] 中的整数；
如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
如果没有输入任何参数，默认就是初始化数组为0个元素"""
# print(bytearray())  # bytearray(b'')
# print(bytearray(3))  # bytearray(b'\x00\x00\x00')
# print(bytearray(4))  # bytearray(b'\x00\x00\x00\x00')
# print(bytearray([1, 2, 3]))  # bytearray(b'\x01\x02\x03')
# print(bytearray([1, 12, 3, 4]))  # bytearray(b'\x01\x0c\x03\x04')
# print(bytearray('runoob', 'utf-8'))  # bytearray(b'runoob')

"""6 class bool([x])
返回一个布尔值，True 或者 False。如果 x 是假的或者被省略，返回 False；其他情况返回 True。
bool 类是 int 的子类。其他类不能继承自它。它只有 False 和 True 两个实例。"""
# print(bool(4))  # True
# print(bool(0))  # False
# print(bool(-1))  # True

"""5 bin(x)
将一个整数转变为一个前缀为“0b”的二进制字符串。"""
# print(bin(14))  # 0b1110
# # 这个是把0b去掉了
# print(format(14, 'b'))  # 1110
# print(format(14, '#b'))  # 0b1110

"""4 ascii(object)可能用不大到
就像函数 repr()，返回一个对象可打印的字符串，
但是 repr() 返回的字符串中非 ASCII 编码的字符，下面的话放这里。"""
# # 会使用 \x、\u 和 \U 来转义 <-- 这句话在上面会报错  我也不知道为什么
# print(ascii('龙王'))  # '\u9f99\u738b'

"""3 any(iterable)
如果 iterable 的任一元素为真则返回 True。 如果迭代器为空，返回 False。
元素除了是 0、空、FALSE 外都算 True
如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true"""
# 和all函数相反，就这样记住就行
# print(any([])) # False
# print(any(())) # False
# print(any([0, 12, 3, 4])) # True

"""2 all(iterable) 元组或列表
如果 iterable 的所有元素为真（或迭代器为空），返回 True
元素除了是 0、空、None、False 外都算 True。
如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；
注意：空元组、空列表返回值为True，这里要特别注意"""
# # 之前美多有一个验证前端参数的部分 就是用的all()
# if all([0, 12, 3, 4]) is True:
#     pass
# print(all([])) # True
# print(all(())) # True
# print(all([0, 12, 3, 4])) # False

"""1 abs(x)  
返回一个数的绝对值。实参可以是整数或浮点数。如果实参是一个复数，返回它的模。"""
# a = float(10)
# print(a)  # 10.0
# b = -10.123
# print(b)  # -10.123
# print(abs(b))  # 10.123
# c = -8
# print(c)  # -8
# print(abs(c))  # -8
# d = 6j
# print(d * d)  # (-36+0j)
# # 有点意思  输出的是浮点类型
# print(abs(d * d))  # 36.0
# print(type(abs(d * d)))  # <class 'float'>
# print(type(d))  # <class 'complex'>
# print(abs(d))  # 6.0
