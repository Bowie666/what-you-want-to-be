"""5 bin(x)
将一个整数转变为一个前缀为“0b”的二进制字符串。"""
print(bin(14))  # 0b1110
# 这个是把0b去掉了
print(format(14, 'b'))  # 1110
print(format(14, '#b'))  # 0b1110

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
