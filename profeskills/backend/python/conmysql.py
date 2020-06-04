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
# db = MySQLdb.connect("localhost", "root", "123456", "pythontest", charset='utf8' )

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