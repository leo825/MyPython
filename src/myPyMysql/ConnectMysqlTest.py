__author__ = 'LX'

import pymysql
# 打开数据库连接
db = pymysql.connect('localhost', 'root', 'root', 'ssm')

# 使用cursor() 方法创建一个游标对象cursor
cursor = db.cursor()

# 使用execute()方法执行SQL查询
cursor.execute('select version()')

# 使用 fetchone()方法来获取单条数据
data = cursor.fetchone()

print("数据库的版本是：%s" % data)

# 关闭数据库
db.close()


