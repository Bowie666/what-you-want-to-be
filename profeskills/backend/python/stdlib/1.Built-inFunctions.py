"""11 @classmethod
把一个方法封装成类方法。就是调用的时候不需要实例化了"""

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
