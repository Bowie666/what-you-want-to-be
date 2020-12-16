"""object.__call__(self[, args...])

Called when the instance is “called” as a function; if this method is defined, x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...).
也就是说当实例被当作函数调用时会被调用，还有就是x(arg1, arg2, ...)和x.__call__(arg1, arg2, ...)是一样的作用的。
"""

# -------------1 这是一个简单的用法 --仅此说明有了call函数 这个类 可以当普通函数来调用，调用的是call里面的方法---------------
# class TestCall:
#     """
#     Args:
#     """
#     def get(self):
#         print('shiyong get method')
#     def __call__(self):
#         print('shiyong __call__ method')

# t = TestCall()
# t.get()  # shiyong get method
# t()  # shiyong __call__ method

# -------------2 作为装饰器使用 真厉害 有点牛皮-------------------------
# 闭包就是函数可以当参数传，类对象是可以做装饰器的
# 经过装饰以后相当于 test_deco = Decot(test_deco)
# class Decot:
#     def __init__(self, func):
#         self.func = func
#         print('init han shu')
#     def __call__(self):
#         print('call han shu')
#         self.func()

# @Decot
# def test_deco():
#     print('test_deco 函数')

# test_deco()
# # init han shu
# # call han shu
# # test_deco 函数

# class DecoPara(object):
#     def __init__(self, name):
#         self.name = name
#         print('DecoPara init han shu')
#     def __call__(self, func):
#         print('DecoPara call han shu')
#         # func()
#         # -----如果不加下面三行 只用上面的会出错------
#         # 由于装饰器参数的存在 装饰器降了一级 这时只需要往__call__里在添加一个函数即可
#         def inner():
#             func()
#         return inner

# @DecoPara('beibei')
# def test_deco_para():
#     print('test_deco_para han shu')

# test_deco_para()
# # DecoPara init han shu
# # DecoPara call han shu
# # test_deco_para han shu