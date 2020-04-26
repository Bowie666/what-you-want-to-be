"""57 setattr(object, name, value)
此函数与 getattr() 两相对应。 其参数为一个对象、一个字符串和一个任意值。
字符串指定一个现有属性或者新增属性。 函数会将值赋给该属性，只要对象允许这种操作。
例如，setattr(x, 'foobar', 123) 等价于 x.foobar = 123。
object -- 对象。
name -- 字符串，对象属性。
value -- 属性值。"""
# class A(object):
#     bar = 1
# a = A()
# getattr(a, 'bar')  # 获取属性 bar 值
# setattr(a, 'bar', 5)  # 设置属性 bar 值
# print(a.bar)  # 5
# # 如果属性不存在会创建一个新的对象属性，并对属性赋值：
# setattr(a, "age", 28)
# print(a.age)  # 28

"""56 class set([iterable])
返回一个新的 set 对象，可以选择带有从 iterable 获取的元素。 set 是一个内置类型。 """
# x = set('runoob')
# y = set('google')
# print(x)  # {'u', 'n', 'b', 'o', 'r'}
# print(type(x))  # <class 'set'>
# print(y)  # {'e', 'o', 'l', 'g'}
# print(x & y)  # 交集#{'o'}
# print(x | y)  # 并集#{'u', 'o', 'b', 'e', 'r', 'g', 'n', 'l'}
# print(x - y)  # 差集#{'u', 'n', 'r', 'b'}
# print(type(x - y))  # <class 'set'>

"""55 round(number[, ndigits])
返回 number 舍入到小数点后 ndigits 位精度的值。 如果 ndigits 被省略或为 None，则返回最接近输入值的整数。
对于支持 round() 的内置类型，值会被舍入到最接近的 10 的负 ndigits 次幂的倍数；
如果与两个倍数的距离相等，则选择偶数 (因此，round(0.5) 和 round(-0.5) 均为 0 而 round(1.5) 为 2)。
任何整数值都可作为有效的 ndigits (正数、零或负数)。 如果 ndigits 被省略或为 None 则返回值将为整数。
否则返回值与 number 的类型相同。
对于一般的 Python 对象 number, round 将委托给 number.__round__。
x -- 数字表达式。
n -- 表示从小数点位数，其中 x 需要四舍五入，默认值为 0。"""
# print(round(70.23456))  # 70
# print(round(56.659, 1))  # 56.7
# print(round(80.264, 2))  # 80.26
# print(round(100.000056, 3))  # 100.0
# print(round(-100.000056, 3))  # -100.0

"""54 reversed(seq)
返回一个反向的 iterator。 seq 必须是一个具有 __reversed__() 方法的对象或者是支持该序列协议
（具有从 0 开始的整数类型参数的 __len__() 方法和 __getitem__() 方法）。
seq -- 要转换的序列，可以是 tuple, string, list 或 range。"""
# # 字符串
# seqString = 'Runoob'
# print(list(reversed(seqString)))  # ['b', 'o', 'o', 'n', 'u', 'R']
# # 元组
# seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
# print(list(reversed(seqTuple)))  # ['b', 'o', 'o', 'n', 'u', 'R']
# # range
# seqRange = range(5, 9)
# print(list(reversed(seqRange)))  # [8, 7, 6, 5]
# # 列表
# seqList = [1, 2, 4, 3, 5]
# print(list(reversed(seqList)))  # [5, 3, 4, 2, 1]

"""53 repr(object)
返回包含一个对象的可打印表示形式的字符串。
对于许多类型来说，该函数会尝试返回的字符串将会与该对象被传递给 eval() 时所生成的对象具有相同的值，
在其他情况下表示形式会是一个括在尖括号中的字符串，其中包含对象类型的名称与通常包括对象名称和地址的附加信息。
类可以通过定义 __repr__() 方法来控制此函数为它的实例所返回的内容。"""
# s = 'RUNOOB'
# print(repr(s))  # 'RUNOOB'
# print(type(repr(s)))  # <class 'str'>
# dict = {'runoob': 'runoob.com', 'google': 'google.com'}
# print(repr(dict))  # {'runoob': 'runoob.com', 'google': 'google.com'}
# print(type(repr(dict)))  # <class 'str'>

"""52 range(stop)  返回的是一个可迭代对象（类型是对象）
range(start, stop[, step])
虽然被称为函数，但 range 实际上是一个不可变的序列类型
start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)"""
# print(range(0, 30))  # range(0, 30)
# print(range(0, 30, 5))  # range(0, 30, 5)
# print(list(range(3)))  # [0, 1, 2]

"""51 class property(fget=None, fset=None, fdel=None, doc=None)  过会好好看看
返回 property 属性。
fget 是获取属性值的函数。
fset 是用于设置属性值的函数。
fdel 是用于删除属性值的函数。
并且 doc 为属性对象创建文档字符串。
一个典型的用法是定义一个托管属性 x:"""
# class C:
#     def __init__(self):
#         self._x = None
#     def getx(self):
#         return self._x
#     def setx(self, value):
#         self._x = value
#     def delx(self):
#         del self._x
#     x = property(getx, setx, delx, "I'm the 'x' property.")
# c = C()
# print(c.x)  # None
# c.x = 'baae'
# del c.x

"""50 print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
将 objects 打印到 file 指定的文本流，以 sep 分隔并在末尾加上 end。 sep, end, file 和 flush 如果存在，它们必须以关键字参数的形式给出。
所有非关键字参数都会被转换为字符串，就像是执行了 str() 一样，并会被写入到流，以 sep 且在末尾加上 end。
sep 和 end 都必须为字符串；它们也可以为 None，这意味着使用默认值。 如果没有给出 objects，则 print() 将只写入 end。
file 参数必须是一个具有 write(string) 方法的对象；如果参数不存在或为 None，则将使用 sys.stdout。
由于要打印的参数会被转换为文本字符串，因此 print() 不能用于二进制模式的文件对象。 对于这些对象，应改用 file.write(...)。
输出是否被缓存通常决定于 file，但如果 flush 关键字参数为真值，流会被强制刷新。
objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
sep -- 用来间隔多个对象，默认值是一个空格。
end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符串。
file -- 要写入的文件对象。
flush -- 输出是否被缓存通常决定于 file，但如果 flush 关键字参数为 True，流会被强制刷新。"""
# print("aaa""bbb")  # aaabbb
# print("aaa", "bbb")  # aaa bbb
# print("www", "runoob", "com", sep=".")  # 设置间隔符www.runoob.com
# import time
# print("---RUNOOB EXAMPLE ： Loading 效果---")
# print("Loading", end="")
# for i in range(20):
#     print(".", end='', flush=True)
#     time.sleep(0.5)

"""49 pow(x, y[, z])
返回 x 的 y 次幂；如果 z 存在，则对 z 取余（比直接 pow(x, y) % z 计算更高效）。
两个参数形式的 pow(x, y) 等价于幂运算符： x**y。
参数必须为数值类型。 对于混用的操作数类型，则适用二元算术运算符的类型强制转换规则。
对于 int 操作数，结果具有与操作数相同的类型（转换后），除非第二个参数为负值；
在这种情况下，所有参数将被转换为浮点数并输出浮点数结果。 例如，10**2 返回 100，但 10**-2 返回 0.01。
如果第二个参数为负值，则第三个参数必须省略。 如果存在 z，则 x 和 y 必须为整数类型，且 y 必须为非负数。"""
# print(pow(2, 3))  # 8
# print(type(pow(2, 3, 5)))  # <class 'int'>
# print(pow(2, 3, 5))  # 3
# # 下面是测试y值为负数，第三个数不能填写
# print(pow(2, -1))  # 0.5
# # print(pow(2, -1, 3))  # ValueError: pow() 2nd argument cannot be negative when 3rd argument specified

"""48 ord(c)
对表示单个 Unicode 字符的字符串，返回代表它 Unicode 码点的整数。
例如 ord('a') 返回整数 97， ord('€') （欧元符号）返回 8364 。这是 chr() 的逆函数。"""
# print(ord('a'))  # 97
# print(ord('€'))  # 8364

"""47 open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
打开 file 并返回对应的 file object。如果该文件不能打开，则触发 OSError。
file 是一个 path-like object，表示将要打开的文件的路径（绝对路径或者当前工作目录的相对路径），也可以是要被封装的整数类型文件描述符。
（如果是文件描述符，它会随着返回的 I/O 对象关闭而关闭，除非 closefd 被设为 False 。）
mode 是一个可选字符串，用于指定打开文件的模式。默认值是 'r' ，这意味着它以文本模式打开并读取。
其他常见模式有：写入 'w' （截断已经存在的文件）；排它性创建 'x' ；
追加写 'a' （在 一些 Unix 系统上，无论当前的文件指针在什么位置，所有 写入都会追加到文件末尾）。
在文本模式，如果 encoding 没有指定，则根据平台来决定使用的编码：使用 locale.getpreferredencoding(False) 来获取本地编码。
（要读取和写入原始字节，请使用二进制模式并不要指定 encoding。）可用的模式有：

字符 含义

'r' 读取（默认）

'w' 写入，并先截断文件

'x' 排它性创建，如果文件已存在则失败

'a' 写入，如果文件存在则在末尾追加

'b' 二进制模式

't' 文本模式（默认）

'+' 更新磁盘文件（读取并写入）

'U' universal newlines mode (deprecated)

默认的模式是 'r' （打开并读取文本，同 'rt' ）。对于二进制写入， 'w+b' 模式打开并把文件截断成 0 字节； 'r+b' 则不会截断。

正如在 概述 中提到的，Python区分二进制和文本I/O。以二进制模式打开的文件（包括 mode 参数中的 'b' ）返回的内容为 bytes`对象，不进行任何解码。
在文本模式下（默认情况下，或者在 *mode* 参数中包含 `’t’` ）时，文件内容返回为 str ，首先使用指定的 encoding （如果给定）或者使用平台默认的的字节编码解码。

注解 Python不依赖于底层操作系统的文本文件概念;所有处理都由Python本身完成，因此与平台无关。
buffering 是一个可选的整数，用于设置缓冲策略。
传递0以切换缓冲关闭（仅允许在二进制模式下），1选择行缓冲（仅在文本模式下可用），并且>1的整数以指示固定大小的块缓冲区的大小（以字节为单位）。
如果没有给出 buffering 参数，则默认缓冲策略的工作方式如下:

二进制文件以固定大小的块进行缓冲；
使用启发式方法选择缓冲区的大小，尝试确定底层设备的“块大小”或使用 io.DEFAULT_BUFFER_SIZE。
在许多系统上，缓冲区的长度通常为4096或8192字节。

“交互式”文本文件（ isatty() 返回 True 的文件）使用行缓冲。
其他文本文件使用上述策略用于二进制文件。

encoding 是用于解码或编码文件的编码的名称。
这应该只在文本模式下使用。默认编码是依赖于平台的（不 管 locale.getpreferredencoding() 返回何值），但可以使用任何Python支持的 text encoding 。
有关支持的编码列表，请参阅 codecs 模块。

errors 是一个可选的字符串参数，用于指定如何处理编码和解码错误 - 这不能在二进制模式下使用。
可以使用各种标准错误处理程序（列在 错误处理方案 ），但是使用 codecs.register_error() 注册的任何错误处理名称也是有效的。
标准名称包括:

如果存在编码错误，'strict' 会引发 ValueError 异常。 默认值 None 具有相同的效果。

'ignore' 忽略错误。请注意，忽略编码错误可能会导致数据丢失。

'replace' 会将替换标记（例如 '?' ）插入有错误数据的地方。

'surrogateescape' 将表示任何不正确的字节作为Unicode专用区中的代码点，范围从U+DC80到U+DCFF。
当在写入数据时使用 surrogateescape 错误处理程序时，这些私有代码点将被转回到相同的字节中。这对于处理未知编码的文件很有用。

只有在写入文件时才支持 'xmlcharrefreplace'。编码不支持的字符将替换为相应的XML字符引用 &#nnn;。

'backslashreplace' 用Python的反向转义序列替换格式错误的数据。

'namereplace' （也只在编写时支持）用 \\N{...} 转义序列替换不支持的字符。

newline 控制 universal newlines 模式如何生效（它仅适用于文本模式）。
它可以是 None，''，'\\n'，'\\r' 和 '\\r\n'。它的工作原理:

从流中读取输入时，如果 newline 为 None，则启用通用换行模式。
输入中的行可以以 '\\n'，'\\r' 或 '\\r\n' 结尾，这些行被翻译成 '\\n' 在返回呼叫者之前。
如果它是 ''，则启用通用换行模式，但行结尾将返回给调用者未翻译。
如果它具有任何其他合法值，则输入行仅由给定字符串终止，并且行结尾将返回给未调用的调用者。

将输出写入流时，如果 newline 为 None，则写入的任何 '\\n' 字符都将转换为系统默认行分隔符 os.linesep。
如果 newline 是 '' 或 '\\n'，则不进行翻译。如果 newline 是任何其他合法值，则写入的任何 '\\n' 字符将被转换为给定的字符串。

如果 closefd 是 False 并且给出了文件描述符而不是文件名，那么当文件关闭时，底层文件描述符将保持打开状态。
如果给出文件名则 closefd 必须为 True （默认值），否则将引发错误。

可以通过传递可调用的 opener 来使用自定义开启器。
然后通过使用参数（ file，flags ）调用 opener 获得文件对象的基础文件描述符。 
opener 必须返回一个打开的文件描述符（使用 os.open as opener 时与传递 None 的效果相同）。
新创建的文件是 不可继承的。"""

"""46 oct(x)
将一个整数转变为一个前缀为“0o”的八进制字符串。结果是一个合法的 Python 表达式。
如果 x 不是 Python 的 int 对象，那它需要定义 __index__() 方法返回一个整数。"""
# print(oct(8))  # 0o10
# print(oct(-56))  # -0o70
# # 如果要将整数转换为八进制字符串，并可选择有无“0o”前缀
# print(format(10, '#o'))  # 0o12
# print(format(10, 'o'))  # 12
# print(f'{10:#o}')  # 0o12
# print(f'{10:o}')  # 12
# print('%#o' % 10)  # 0o12
# print('%o' % 10)  # 12
# print(type('%#o' % 10))  # <class 'str'>
# print(type('%o' % 10))  # <class 'str'>

"""45 class object
返回一个没有特征的新对象。object 是所有类的基类。它具有所有 Python 类实例的通用方法。这个函数不接受任何实参。
注解 由于 object 没有 __dict__，因此无法将任意属性赋给 object 的实例。"""
# 这个东西没有任何特征

"""44 next(iterator[, default])
通过调用 iterator 的 __next__() 方法获取下一个元素。
如果迭代器耗尽，则返回给定的 default，如果没有默认值则触发 StopIteration。"""
# it = iter([1, 2, 3, 4, 5])
# print(next(it))  # 1
# # while True:
# #     print(next(it))  # 这种会报错
# while True:
#     try:
#         # 获得下一个值:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         # 遇到StopIteration就退出循环
#         break

"""43 min(iterable, *[, key, default]) 返回给定参数的最小值。这个和max类似
min(arg1, arg2, *args[, key])
返回可迭代对象中最小的元素，或者返回两个及以上实参中最小的。
如果只提供了一个位置参数，它必须是 iterable，返回可迭代对象中最小的元素；
如果提供了两个及以上的位置参数，则返回最小的位置参数。
有两个可选只能用关键字的实参。key 实参指定排序函数用的参数，如传给 list.sort() 的。
default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。
如果有多个最小元素，则此函数将返回第一个找到的。
这和其他稳定排序工具如 sorted(iterable, key=keyfunc)[0] 和 heapq.nsmallest(1, iterable, key=keyfunc) 保持一致。"""
# print(min(80, 100, 1000))  # 80
# print(min(-20, 100, 400))  # -20
# print(min(-80, -20, -10))  # -80
# print(min(0, 100, -400))  # -400

"""42 memoryview(obj) 不太懂
返回由给定实参创建的“内存视图”对象
函数返回给定参数的内存查看对象(Momory view)。
所谓内存查看对象，是指对支持缓冲区协议的数据进行包装，在不需要复制对象基础上允许Python代码访问"""
# # v = memoryview('abcefg')
# # print(v[2])  # TypeError: memoryview: a bytes-like object is required, not 'str'
# g = memoryview('abcefg'.encode())
# print(g[2])  # 99
# a = memoryview(bytearray('abcefg', encoding='utf-8'))
# print(a[2])  # 99

"""41 max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
返回可迭代对象中最大的元素，或者返回两个及以上实参中最大的。
如果只提供了一个位置参数，它必须是非空 iterable，返回可迭代对象中最大的元素；
如果提供了两个及以上的位置参数，则返回最大的位置参数。
有两个可选只能用关键字的实参。key 实参指定排序函数用的参数，如传给 list.sort() 的。
default 实参是当可迭代对象为空时返回的值。如果可迭代对象为空，并且没有给 default ，则会触发 ValueError。
如果有多个最大元素，则此函数将返回第一个找到的。这和其他稳定排序工具如:
sorted(iterable, key=keyfunc, reverse=True)[0] 和 heapq.nlargest(1, iterable, key=keyfunc) 保持一致。"""
# print("max(80, 100, 1000) : ", max([80, 100, 1000], [80, 100, 1001, 55]))  # max(80, 100, 1000) :  [80, 100, 1001, 55]
# print("max(-20, 100, 400) : ", max(-20, 100, 400))  # max(-20, 100, 400) :  400
# print("max(-80, -20, -10) : ", max(-80, -20, -10))  # max(-80, -20, -10) :  -10
# print("max(0, 100, -400) : ", max(0, 100, -400))  # max(0, 100, -400) :  100

"""40 map(function, iterable, ...)   function -- 函数  iterable -- 一个或多个序列
返回一个将 function 应用于 iterable 中每一项并输出其结果的迭代器。
如果传入了额外的 iterable 参数，function 必须接受相同个数的实参并被应用于从所有可迭代对象中并行获取的项。
当有多个可迭代对象时，最短的可迭代对象耗尽则整个迭代就将结束。"""
# def square(x):  # 计算平方数
#     return x ** 2
# print(type(map(square, [1, 2, 3, 4, 5])))  # <class 'map'>计算列表各个元素的平方
# print([i for i in map(lambda x: x ** 2, [1, 2, 3, 4, 5])])  # [1, 4, 9, 16, 25]使用 lambda 匿名函数
# # 提供了两个列表，对相同位置的列表数据进行相加<map object at 0x0000000001DBC208>
# print(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))


"""39 locals() 函数会以字典类型返回当前位置的全部局部变量。
对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。
注解 不要更改此字典的内容；更改不会影响解释器使用的局部变量或自由变量的值。"""
# def runoob(arg):  # 两个局部变量：arg、z
#     z = 1
#     print(locals())
# runoob(4)  # 返回一个名字/值对的字典{'z': 1, 'arg': 4}

"""38 class list([iterable]) 要转换为列表的元组或字符串。方法用于将元组或字符串转换为列表。
虽然被称为函数，list 实际上是一种可变序列类型，详情请参阅 列表 和 序列类型 — list, tuple, range。"""
# 不太好整理
# aTuple = (123, 'Google', 'Runoob', 'Taobao')
# list1 = list(aTuple)
# print("列表元素 : ", list1)  # [123, 'Google', 'Runoob', 'Taobao']
# str = "Hello World"
# list2 = list(str)
# print("列表元素 : ", list2)  # ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

"""37 len(s)
返回对象的长度（元素个数）。
实参可以是序列（如 string、bytes、tuple、list 或 range 等）或集合（如 dictionary、set 或 frozen set 等）。"""
# str = "runoob"
# print(len(str))  # 6
# l = [1, 2, 3, 4, 5]
# print(len(l))  # 5

"""36 iter(object[, sentinel])
返回一个 iterator 对象。根据是否存在第二个实参，第一个实参的解释是非常不同的。
如果没有第二个实参，object 必须是支持迭代协议（有 __iter__() 方法）的集合对象，
或必须支持序列协议（有 __getitem__() 方法，且数字参数从 0 开始）。
如果它不支持这些协议，会触发 TypeError。
如果有第二个实参 sentinel，那么 object 必须是可调用的对象。
这种情况下生成的迭代器，每次迭代调用它的 __next__() 方法时都会不带实参地调用 object；
如果返回的结果是 sentinel 则触发 StopIteration，否则返回调用结果。"""
# lst = [1, 2, 3]
# def test():
#     return 4
# for i in iter(lst):  # 竖着打印1 2 3
#     print(i)
# # for i in iter(test, ''):  # 不管后面是什么参数这样会一直打印4
# #     print(i)
# for i in iter(test):  # TypeError: 'function' object is not iterable
#     print(i)

"""35 issubclass(class, classinfo) class -- 类。classinfo -- 类。
 issubclass() 方法用于判断参数 class 是否是类型参数 classinfo 的子类。
 """
# class A:
#     pass
# class B(A):
#     pass
# print(issubclass(B, A))  # True
# print(issubclass(A, B))  # False

"""34 isinstance(object, classinfo)
isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
isinstance() 与 type() 区别：
    type() 不会认为子类是一种父类类型，不考虑继承关系。
    isinstance() 会认为子类是一种父类类型，考虑继承关系。
如果要判断两个类型是否相同推荐使用 isinstance()。"""
# a = 2
# print(isinstance(a, int))  # True
# print(isinstance(a, str))  # False
# print(isinstance(a, (str, int, list)))  # 是元组中的一个返回 True
# class A:
#     pass
# class B(A):
#     pass
# print(isinstance(A(), A))  # True
# print(type(A()) == A)  # True
# print(isinstance(B(), A))  # True
# print(type(B()) == A)  # False

"""33 class int(x=0)
class int(x, base=10)    x -- 字符串或数字。base -- 进制数，默认十进制。
返回一个使用数字或字符串 x 生成的整数对象，或者没有实参的时候返回 0 。
如果 x 定义了 __int__()，int(x) 返回 x.__int__() 。
如果 x 定义了 __trunc__()，它返回 x.__trunc__() 。对于浮点数，它向零舍入。
如果 x 不是数字，或者有 base 参数，x 必须是字符串、bytes、表示进制为 base 的 整数字面值 的 bytearray 实例。
该文字前可以有 + 或 - （中间不能有空格），前后可以有空格。
一个进制为 n 的数字包含 0 到 n-1 的数，其中 a 到 z （或 A 到 Z ）表示 10 到 35。
默认的 base 为 10 ，允许的进制有 0、2-36。
2、8、16 进制的数字可以在代码中用 0b/0B 、 0o/0O 、 0x/0X 前缀来表示。
进制为 0 将安照代码的字面量来精确解释，最后的结果会是 2、8、10、16 进制中的一个。
所以 int('010', 0) 是非法的，但 int('010') 和 int('010', 8) 是合法的。"""
# # 说的比较麻烦 但大概就下面几个例子
# print(int())  # 不传入参数时，得到结果0
# print(int(3))  # 3
# print(int(3.6))  # 3
# print(int('12', 16))  # 18 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
# print(int('0xa', 16))  # 10
# print(int('10', 8))  # 8

"""32 input([prompt])   接受一个标准输入数据，返回为 string 类型。prompt: 提示信息
如果存在 prompt 实参，则将其写入标准输出，末尾不带换行符。
接下来，该函数从输入中读取一行，将其转换为字符串（除了末尾的换行符）并返回。
当读取到 EOF 时，则触发 EOFError。例如:"""
# a = input("input:")  # 输入整数
# print(type(a))  # 字符串
# a = input("input:")  # 正确，字符串表达式
# print(type(a))  # 字符串

"""31 id(object)
返回对象的内存地址。
返回对象的“标识值”。该值是一个整数，在此对象的生命周期中保证是唯一且恒定的。
两个生命期不重叠的对象可能具有相同的 id() 值。"""
# a = 10
# print(id(a))  # 1814528400

"""30 hex(x)
将整数转换为以“0x”为前缀的小写十六进制字符串。
hex() 函数用于将一个指定数字转换为 16 进制数。
如果 x 不是 Python int 对象，则必须定义返回整数的 __index__() 方法。
如果要获取浮点数的十六进制字符串形式，请使用 float.hex() 方法。"""
# print(hex(255))  # 0xff
# print(hex(-42))  # -0x2a
# print(hex(12))  # 0xc
# print(hex(-12))  # -0xc
# print(type(hex(12)))  # <class 'str'>
# print(hex(9))  # 0x9
# print(float.hex(0.5))  # 0x1.0000000000000p-1
# print(hex('u'))  # TypeError: 'str' object cannot be interpreted as an integer

"""29 help([object])
启动内置的帮助系统（此函数主要在交互式中使用）。如果没有实参，解释器控制台里会启动交互式帮助系统。
如果实参是一个字符串，则在模块、函数、类、方法、关键字或文档主题中搜索该字符串，并在控制台上打印帮助信息。
如果实参是其他任意对象，则会生成该对象的帮助页。该函数通过 site 模块加入到内置命名空间。"""
# help('sys')  # 查看 sys 模块的帮助 加不加print都可以
# # ……显示帮助信息……
# help('str')  # 查看 str 数据类型的帮助
# # ……显示帮助信息……
# a = [1, 2, 3]
# help(a)  # 查看列表 list 帮助信息
# # ……显示帮助信息……
# help(a.append)  # 显示list的append方法的帮助
# # ……显示帮助信息……
# print(help(set))

"""28 hash(object)
返回该对象的哈希值（如果它有的话）。哈希值是整数。它们在字典查找元素时用来快速比较字典的键。
相同大小的数字变量有相同的哈希值（即使它们类型不同，如 1 和 1.0）。"""
# print(hash('test'))  # 字符串 8726183001633535878
# print(hash(1))  # 数字1
# print(hash(str([1, 2, 3])))  # 集合2528267408979111709
# print(hash(str(sorted({'1': 1}))))  # 字典480096517480272175

"""27 hasattr(object, name)   函数用于判断对象是否包含对应的属性。object -- 对象。name -- 字符串，属性名。
该实参是一个对象和一个字符串。如果字符串是对象的属性之一的名称，则返回 True，否则返回 False。
（此功能是通过调用 getattr(object, name) 看是否有 AttributeError 异常来实现的。）"""
# class Coordinate:
#     x = 10
#     y = -5
#     z = 0
# point1 = Coordinate()
# print(hasattr(point1, 'x'))  # True
# print(hasattr(point1, 'y'))  # True
# print(hasattr(point1, 'z'))  # True
# print(hasattr(point1, 'no'))  # 没有该属性False

"""26 globals()
返回表示当前全局符号表的字典。这总是当前模块的字典（在函数或方法中，不是调用它的模块，而是定义它的模块）。"""
# a = 'runoob'
# print(globals(a))  # TypeError: globals() takes no arguments (1 given)
# print(globals())
# #  globals 函数返回一个全局变量的字典，包括所有导入的变量。
# # {'__builtins__': <module '__builtin__' (built-in)>,
# # '__name__': '__main__', '__doc__': None, 'a': 'runoob', '__package__': None}

"""25 getattr(object, name[, default])
返回对象命名属性的值。name 必须是字符串。如果该字符串是对象的属性之一，则返回该属性的值。
例如， getattr(x, 'foobar') 等同于 x.foobar。
如果指定的属性不存在，且提供了 default 值，则返回它，否则触发 AttributeError。"""
# class B(object):
#     bar = 1
# a1 = B()
# print(getattr(a1, 'bar'))  # 获取属性 bar 值   1
# print(getattr(a1, 'bar2'))  # 属性 bar2 不存在，触发异常 AttributeError: 'B' object has no attribute 'bar2'
# print(getattr(a1, 'bar2', 3))  # 属性 bar2 不存在，但设置了默认值  3

# class A(object):
#     def set(self, a, b):
#         x = a
#         a = b
#         b = x
#         print(a, b)
# d = A()
# c = getattr(d, 'set')
# print(c)  # <bound method A.set of <__main__.A object at 0x000000000ADBF898>>
# print(type(c))  # <class 'method'>
# print(c(a='1', b='2'))  # None
# print(type(c(a='1', b='2')))  # <class 'NoneType'>

"""24 class frozenset([iterable])    ---------有待琢磨
返回一个新的 frozenset 对象，它包含可选参数 iterable 中的元素。iterable -- 可迭代的对象，比如列表、字典、元组等等。
frozenset() 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。"""
# a = frozenset(range(10))  # 生成一个新的不可变集合
# print(a)  # frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})
# b = frozenset('runoob')
# print(b)  # frozenset({'u', 'b', 'o', 'r', 'n'})   # 创建不可变集合

"""23 format(value[, format_spec])  -------这个东西有待整理，应该还有别的功能
将 value 转换为 format_spec 控制的“格式化”表示。
format_spec 的解释取决于 value 实参的类型，但是大多数内置类型使用标准格式化语法：格式规格迷你语言。
默认的 format_spec 是一个空字符串，它通常和调用 str(value) 的结果相同。"""
# print("{} {}".format("hello", "world"))  # 不设置指定位置，按默认顺序
# print("{0} {1}".format("hello", "world"))  # 设置指定位置
# print("{1} {0} {1}".format("hello", "world"))  # 设置指定位置
# print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))
#
# site = {"name": "菜鸟教程", "url": "www.runoob.com"}  # 通过字典设置参数
# print("网站名：{name}, 地址 {url}".format(**site))
#
# my_list = ['菜鸟教程', 'www.runoob.com']  # 通过列表索引设置参数
# print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

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
