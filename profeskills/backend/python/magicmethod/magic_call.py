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


# ---------------- 下面是资料 ------------------------------
# Python中对象按能否被调用可分为可调用对象与不可调用的对象（这不废话吗）

# 举一个栗子

# class A(object):
#     def __init__(self):
#         pass
# a = A()
# print('A能被调用吗?',callable(A))
# print('a能被调用吗?',callable(a))
#结果为：
#A能被调用吗? True
#a能被调用吗? False
# 这说明类对象（函数也可以的）可以被调用，而类的实例不能不调用，若想要实例对象被调用，只需在类的定义里加上__call__函数即可

# class A(object):
#     def __init__(self):
#         pass
#     def __call__(self):
#         pass
# a = A()
# print('A能被调用吗?',callable(A))
# print('a能被调用吗?',callable(a))
# #结果为：
# #A能被调用吗? True
# #a能被调用吗? True
# 咦，这是咋回事？

# 咋回事？
# 我去python官方文档上查了一哈：



# 来个栗子会更加清楚：

# class Friend(object):
#     def __init__(self,name,male):
#         self.name = name
#         self.male = male
#         print('我叫',self.name)
#         print('我的性别是',self.male)
#     def __call__(self,friendname):
#         self.friendname = friendname
#         print('我叫{}，我的朋友是{}'.format(self.name,self.friendname))
# a = Friend('康康','男')
# a('小明')
# a.__call__('小明')
# #结果为：
# #我叫 康康
# #我的性别是 男
# #我叫康康，我的朋友是小明
# #我叫康康，我的朋友是小明
# 在例子中

# a('小明') 和 a.__call__('小明') 得到的结果是一样的

# a由于有__call__的存在成为了一个可以当作函数的实例。

# 那这个__call__就这点用处了？No No No(●ˇ∀ˇ●)

# __call__作用下的装饰器
# 没听说过吧╰(￣ω￣ｏ)

# class decorator(object):
#     def __init__(self,func):
#         self.func = func
#     def __call__(self):
#         print('我是在call里被打印的')
#         self.func()
# @decorator  #经过装饰以后相当于test = decorator(test)
# def test():
#     print('我是被装饰的函数')
# test()
# 结果就是：

# 我是在call里被打印的
# 我是被装饰的函数
# 牛批吧，都是血和泪的教训

# 当装饰器有参数时（@bala('参数')）
# class decorator(object):
#     def __init__(self, name):
#         self.name = name
#         print('传来的参数是：',self.name)
#     def __call__(self, func):
#         print('到我call的地盘了')
#         print('传来的参数是：',func)

# @decorator('parm')
# def param_check():
#     print('Hello')
# #结果为：
# #传来的参数是： parm
# #到我call的地盘了
# #传来的参数是： <function param_check at 0x006223D8>
# 分析一下：

# 装饰器语句的参数被传递到了__init__中
# 被装饰的函数作为参数传递到了__call__中
# But加上 param_check()出现的是

# class decorator(object):
#     def __init__(self, name):
#         self.name = name
#         print('传来的参数是：',self.name)
#     def __call__(self, func):
#         print('到我call的地盘了')
#         print('传来的参数是：',func)

# @decorator('parm')
# def param_check():
#     print('Hello')
# param_check()
# 传来的参数是： parm
# 到我call的地盘了
# 传来的参数是： <function param_check at 0x02C723D8>
# TypeError: 'NoneType' object is not callable
#  按照前面的例子来说不应该出错的，肯定是还没有弄懂它的原理。。。

# 看过这个文章后大致明白了一些 https://blog.csdn.net/Eclipsesy/article/details/79238690

# 由于装饰器参数的存在，装饰器降了一级（看不明白吧，我也不大明白），这时只需要往__call__里在添加一个函数即可

# 即：

# class decorator(object):
#     def __init__(self,name):
#         self.name = name
#         print('传来的参数是：',self.name)
#     def __call__(self, func):
#         print('到我call的地盘了')
#         print('传来的参数是：',func)
#         def inner():
#             func()
#         return inner

# @decorator('parm')  
# def param_check():
#     print('Hello')
# param_check()
# #就可得到结果：
# #传来的参数是： parm
# #到我call的地盘了
# #传来的参数是： <function param_check at 0x035C23D8>
# #Hello
# 就酱！

