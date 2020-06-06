import pymysql
import MySQLdb
# # 1 连接数据库 实例：
# # 以下实例链接Mysql的TESTDB数据库：
# # import MySQLdb
# # 打开数据库连接
# # db = MySQLdb.connect("localhost", "root", "123456", "pythontest", charset='utf8' )
# db = pymysql.connect("localhost", "root", "123456", "pythontest", charset='utf8' )
# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()
# # 使用execute方法执行SQL语句
# cursor.execute("SELECT VERSION()")

# # 使用 fetchone() 方法获取一条数据
# data = cursor.fetchone()

# print("Database version : %s " % data)

# # 关闭数据库连接
# db.close()


# # 2 创建数据库表
# # 如果数据库连接存在我们可以使用execute()方法来为数据库创建表，如下所示创建表EMPLOYEE：

# #!/usr/bin/python
# # -*- coding: UTF-8 -*-

# import MySQLdb

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123456", "pythontest", charset='utf8')

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # 如果数据表已经存在使用 execute() 方法删除表。
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# # 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,  
#          SEX CHAR(1),
#          INCOME FLOAT )"""

# cursor.execute(sql)

# # 关闭数据库连接
# db.close()


# # 3 数据库插入操作
# # 以下实例使用执行 SQL INSERT 语句向表 EMPLOYEE 插入记录：

# import random


# # dat1 = 'abcdefghijklmnopqrstuvwxyz'
# # dat2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# # dat3 = '0123456789'
# # # random.choice()
# # # 多个字符中选取指定数量的字符组成新字符串：
# # print(''.join(random.sample(['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a'], 5)))
# # print(''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 5)))


# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123456", "cloud", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# dat = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# for i in range(20):
#     name = ''.join(random.sample(dat, 5))
#     api = ''.join(random.sample(dat, 8))
#     introduct = ''.join(random.sample(dat, 10))
#     # SQL 插入语句
#     sql = """INSERT INTO algomod(name, api, introduct, is_delete, ctime, utime) VALUES ('%s', '%s', '%s', 0, NOW(), NOW())""" % (name, api, introduct)
#     print(sql)
#     try:
#         # 执行sql语句
#         cursor.execute(sql)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # Rollback in case there is any error
#         db.rollback()

# # 关闭数据库连接
# db.close()

# # 3（变）以上例子也可以写成如下形式：

# import MySQLdb

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123456", "pythontest", charset='utf8')

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 插入语句
# sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('%s', '%s', %s, '%s', %s )" % ('Jack', 'Sparrow', 20, 'M', 2000)
# # sql = "INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (%s, %s, %s, %s, %s )" % ('Jack', 'Sparrow', 20, 'M', 2000)  # 这个是错的 关键是引号
# # INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES (Jack, Sparrow, 20, M, 2000 )  # 这个是错的
# # INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('Jack', 'Sparrow', 20, 'M', 2000 )  # 这个是对的
# # sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME, AGE, SEX, INCOME) VALUES ('Mac', 'Mohan', 20, 'M', 2000)"  # 这个是对的
# print(sql)
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
#    print(1)
# except:
#    # 发生错误时回滚
#    db.rollback()
#    print(2)

# # 关闭数据库连接
# db.close()

# # 4 数据库查询操作
# # Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。

# # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
# # fetchall():接收全部的返回结果行.
# # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
# # 实例：
# # 查询EMPLOYEE表中salary（工资）字段大于1000的所有数据：

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123456", "pythontest", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 查询语句
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > %s" % (1000)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    print(results)  # (('Mac', 'Mohan', 20, 'M', 2000.0), ('Mac', 'Mohan', 20, 'M', 2000.0), ('Jack', 'Sparrow', 20, 'M', 2000.0))
#    for row in results:
#       fname = row[0]
#       lname = row[1]
#       age = row[2]
#       sex = row[3]
#       income = row[4]
#       # 打印结果
#       print("fname=%s,lname=%s,age=%s,sex=%s,income=%s" % (fname, lname, age, sex, income ))
# except:
#    print("Error: unable to fecth data")

# # 关闭数据库连接
# db.close()



# # 5 数据库更新操作
# # 更新操作用于更新数据表的的数据，以下实例将 EMPLOYEE 表中的 SEX 字段为 'M' 的 AGE 字段递增 1：

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123456", "cloud", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 更新语句
# sql = "UPDATE algomod SET is_delete = 1 WHERE id < %s" % (4)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

# # 关闭数据库连接
# db.close()


# # 6 删除操作用于删除数据表中的数据，以下实例演示了删除数据表 EMPLOYEE 中 AGE 大于 20 的所有数据：

# # 打开数据库连接
# db = MySQLdb.connect("localhost", "root", "123456", "pythontest", charset='utf8' )

# # 使用cursor()方法获取操作游标 
# cursor = db.cursor()

# # SQL 删除语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 提交修改
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()

# # 关闭连接
# db.close()


# 7 执行事务
# 事务机制可以确保数据一致性。

# 事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。

# 原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
# 一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
# 隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
# 持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
# Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。

# 实例：
# # SQL删除记录语句
# sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 向数据库提交
#    db.commit()
# except:
#    # 发生错误时回滚
#    db.rollback()
# 对于支持事务的数据库， 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务。

# commit()方法游标的所有更新操作，rollback（）方法回滚当前游标的所有操作。每一个方法都开始了一个新的事务。

# 错误处理
# DB API中定义了一些数据库操作的错误及异常，下表列出了这些错误和异常:

# 异常	描述
# Warning	当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
# Error	警告以外所有其他错误类。必须是 StandardError 的子类。
# InterfaceError	当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
# DatabaseError	和数据库有关的错误发生时触发。 必须是Error的子类。
# DataError	当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
# OperationalError	指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
# IntegrityError	完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
# InternalError	数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
# ProgrammingError	程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
# NotSupportedError	不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。