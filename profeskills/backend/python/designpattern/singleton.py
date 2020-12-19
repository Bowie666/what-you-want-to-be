"""单例模式
单例模式是指:保证一个类仅有一个实例，并提供一个访问它的全局访问点
单例相当于一个全局变量 但是防止了命名空间被污染

单例模式的优点:
1、由于单例模式要求在全局内只有一个实例，因而可以节省比较多的内存空间
2、全局只有一个接入点，可以更好地进行数据同步控制，避免多重占用
3、单例可长驻内存，减少系统开销

单例模式的缺点:
1、单例模式的扩展是比较困难的
2、赋于了单例以太多的职责，某种程度上违反单一职责原则（六大原则后面会讲到）;
3、单例模式是并发协作软件模块中需要最先完成的，因而其不利于测试
4、单例模式在某种情况下会导致“资源瓶颈”

单例模式的应用举例:
1、生成全局惟一的序列号
2、访问全局复用的惟一资源，如磁盘、总线等
3、单个对象占用的资源过多，如数据库等
4、系统全局统一管理，如Windows下的Task Manager
5、网站计数器
"""
class Singleton:
    # new方法第一个的参数是一个类
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


# # 这种情况是单例只能实例化一次 所以33把10给替掉了
# class Dog(Singleton):
#     def __init__(self, a):
#         self.a = a

# d1 = Dog(10)
# d2 = Dog(33)

# print(d1.a, d2.a)  # 33 33
# print(id(d1.a), id(d2.a))  # 1544062064 1544062064




# ----------------下面的都是之前测试的数据------------------
# ------------------第一种---------------------
# class S:
#     instance = None
#     def __new__(cls, *args, **kwargs):
#         if S.instance is None:
#             S.instance = super().__new__(cls)

#     def __init__(self):
#         pass

# s1 = S()
# print(id(s1))  # 1582333232
# s2 = S()
# print(id(s2))  # 1582333232

# --------------------第二种---------------
# new方法第一个参数cls是一个类
# class Singlee(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singlee, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance

# s3 = Singlee()
# print(id(s3))  # 1582333232
# s4 = Singlee()
# print(id(s4))  # 1582333232


# class Dog:
#     def __init__(self):
#         self.kind = '小狗'
#         self.sound = '旺旺'
# d1 = Dog()
# print(id(d1), d1.kind)  # 43609504 小狗
# d2 = Dog()
# print(id(d2), d1.sound)  # 43609728 旺旺

# class Singletion:
#     _instance = None

#     @classmethod
#     def instance(cls):
#         if not cls._instance:
#             cls._instance = cls()
#         return cls._instance

# a = Singletion.instance()
# b = Singletion.instance()
# print(id(a),id(b))

# class Singleton(object):
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kw)
#         return cls._instance

# class Singleton3:
#     def __new__(cls, *args, **kw):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super(Singleton3, cls).__new__(cls)
#         return cls._instance

# class Mon(Singleton3):
#     def __init__(self, a=0):
#         self.a = a

# sig = Mon(3)
# sif = Mon(4)

# print(sig.a, sif.a)
# print(id(sig.a), id(sif.a))


# class Singleto():
#     def __new__(cls, *args, **kw):
#         if hasattr(Singleto, '_instance'):
#             tabd = super(Singleto, cls)
#             cls._instance = tabd.__new__(cls, *args, **kw)
#         return cls._instance

# --------------------下面是一个文章作者介绍的很好
# 单例模式（Singleton Pattern）是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。
# 当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场。

# 比如，某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。如果在程序运行期间，有很多地方都需要使用配置文件的内容
# 也就是说，很多地方都需要创建 AppConfig 对象的实例，这就导致系统中存在多个 AppConfig 的实例对象，而这样会严重浪费内存资源，尤其是在配置文件内容很多的情况下。
# 事实上，类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。

# 在 Python 中，我们可以用多种方法来实现单例模式

 

# 其实，Python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。
# 因此，我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。如果我们真的想要一个单例类，可以考虑这样做：

# mysingleton.py

# class Singleton(object):
#     def foo(self):
#         pass
# singleton = Singleton()
# 将上面的代码保存在文件 mysingleton.py 中，要使用时，直接在其他文件中导入此文件中的对象，这个对象即是单例模式的对象

# from a import singleton
 

# def Singleton(cls):
#     _instance = {}

#     def _singleton(*args, **kargs):
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kargs)
#         return _instance[cls]

#     return _singleton


# @Singleton
# class A(object):
#     a = 1

#     def __init__(self, x=0):
#         self.x = x


# a1 = A(2)
# a2 = A(3)
 

 

# class Singleton(object):

#     def __init__(self):
#         pass

#     @classmethod
#     def instance(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance
# 一般情况，大家以为这样就完成了单例模式，但是这样当使用多线程时会存在问题

 

# class Singleton(object):

#     def __init__(self):
#         pass

#     @classmethod
#     def instance(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance

# import threading

# def task(arg):
#     obj = Singleton.instance()
#     print(obj)

# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()
# 程序执行后，打印结果如下：

# <__main__.Singleton object at 0x02C933D0>
# <__main__.Singleton object at 0x02C933D0>
# <__main__.Singleton object at 0x02C933D0>
# <__main__.Singleton object at 0x02C933D0>
# <__main__.Singleton object at 0x02C933D0>
# <__main__.Singleton object at 0x02C933D0>
# <__main__.Singleton object at 0x02C933D0>
# <__main__.Singleton object at 0x02C933D0>
# <__main__.Singleton object at 0x02C933D0>
# <__main__.Singleton object at 0x02C933D0>
# 看起来也没有问题，那是因为执行速度过快，如果在init方法中有一些IO操作，就会发现问题了，下面我们通过time.sleep模拟

# 我们在上面__init__方法中加入以下代码：

#     def __init__(self):
#         import time
#         time.sleep(1)
# 重新执行程序后，结果如下

# <__main__.Singleton object at 0x034A3410>
# <__main__.Singleton object at 0x034BB990>
# <__main__.Singleton object at 0x034BB910>
# <__main__.Singleton object at 0x034ADED0>
# <__main__.Singleton object at 0x034E6BD0>
# <__main__.Singleton object at 0x034E6C10>
# <__main__.Singleton object at 0x034E6B90>
# <__main__.Singleton object at 0x034BBA30>
# <__main__.Singleton object at 0x034F6B90>
# <__main__.Singleton object at 0x034E6A90>
# 问题出现了！按照以上方式创建的单例，无法支持多线程

 

# 解决办法：加锁！未加锁部分并发执行,加锁部分串行执行,速度降低,但是保证了数据安全

# import time
# import threading
# class Singleton(object):
#     _instance_lock = threading.Lock()

#     def __init__(self):
#         time.sleep(1)

#     @classmethod
#     def instance(cls, *args, **kwargs):
#         with Singleton._instance_lock:
#             if not hasattr(Singleton, "_instance"):
#                 Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance


# def task(arg):
#     obj = Singleton.instance()
#     print(obj)
# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()
# time.sleep(20)
# obj = Singleton.instance()
# print(obj)
 

# 打印结果如下：

# <__main__.Singleton object at 0x02D6B110>
# <__main__.Singleton object at 0x02D6B110>
# <__main__.Singleton object at 0x02D6B110>
# <__main__.Singleton object at 0x02D6B110>
# <__main__.Singleton object at 0x02D6B110>
# <__main__.Singleton object at 0x02D6B110>
# <__main__.Singleton object at 0x02D6B110>
# <__main__.Singleton object at 0x02D6B110>
# <__main__.Singleton object at 0x02D6B110>
# <__main__.Singleton object at 0x02D6B110>
# 这样就差不多了，但是还是有一点小问题，就是当程序执行时，执行了time.sleep(20)后，下面实例化对象时
# 此时已经是单例模式了，但我们还是加了锁，这样不太好，再进行一些优化，把intance方法，改成下面的这样就行：

#     @classmethod
#     def instance(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = Singleton(*args, **kwargs)
#         return Singleton._instance
# 这样，一个可以支持多线程的单例模式就完成了

#  完整代码
 

# 这种方式实现的单例模式，使用时会有限制，以后实例化必须通过 obj = Singleton.instance()

# 如果用 obj=Singleton() ,这种方式得到的不是单例

 

# 通过上面例子，我们可以知道，当我们实现单例时，为了保证线程安全需要在内部加入锁

# 我们知道，当我们实例化一个对象时，是先执行了类的__new__方法（我们没写时，默认调用object.__new__）
# 实例化对象；然后再执行类的__init__方法，对这个对象进行初始化，所有我们可以基于这个，实现单例模式

# import threading
# class Singleton(object):
#     _instance_lock = threading.Lock()

#     def __init__(self):
#         pass


#     def __new__(cls, *args, **kwargs):
#         if not hasattr(Singleton, "_instance"):
#             with Singleton._instance_lock:
#                 if not hasattr(Singleton, "_instance"):
#                     Singleton._instance = object.__new__(cls)  
#         return Singleton._instance

# obj1 = Singleton()
# obj2 = Singleton()
# print(obj1,obj2)

# def task(arg):
#     obj = Singleton()
#     print(obj)

# for i in range(10):
#     t = threading.Thread(target=task,args=[i,])
#     t.start()
# 打印结果如下：

# <__main__.Singleton object at 0x038B33D0> <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
# <__main__.Singleton object at 0x038B33D0>
 

# 采用这种方式的单例模式，以后实例化对象时，和平时实例化对象的方法一样 obj = Singleton() 

 

# """
# 1.类由type创建，创建类时，type的__init__方法自动执行，类() 执行type的 __call__方法(类的__new__方法,类的__init__方法)
# 2.对象由类创建，创建对象时，类的__init__方法自动执行，对象()执行类的 __call__ 方法
# """
# 例子：

# class Foo:
#     def __init__(self):
#         pass

#     def __call__(self, *args, **kwargs):
#         pass

# obj = Foo()
# # 执行type的 __call__ 方法，调用 Foo类（是type的对象）的 __new__方法，用于创建对象，然后调用 Foo类（是type的对象）的 __init__方法，用于对对象初始化。

# obj()    # 执行Foo的 __call__ 方法    
 

# 元类的使用

# class SingletonType(type):
#     def __init__(self,*args,**kwargs):
#         super(SingletonType,self).__init__(*args,**kwargs)

#     def __call__(cls, *args, **kwargs): # 这里的cls，即Foo类
#         print('cls',cls)
#         obj = cls.__new__(cls,*args, **kwargs)
#         cls.__init__(obj,*args, **kwargs) # Foo.__init__(obj)
#         return obj

# class Foo(metaclass=SingletonType): # 指定创建Foo的type为SingletonType
#     def __init__(self，name):
#         self.name = name
#     def __new__(cls, *args, **kwargs):
#         return object.__new__(cls)

# obj = Foo('xx')
 

# import threading

# class SingletonType(type):
#     _instance_lock = threading.Lock()
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             with SingletonType._instance_lock:
#                 if not hasattr(cls, "_instance"):
#                     cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
#         return cls._instance

# class Foo(metaclass=SingletonType):
#     def __init__(self,name):
#         self.name = name


# obj1 = Foo('name')
# obj2 = Foo('name')
# print(obj1,obj2)
 

 


# __EOF__

# 本文作者：听风。
# 本文链接：https://www.cnblogs.com/huchong/p/8244279.html