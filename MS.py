# -*- coding:utf-8 -*-
import pymysql
import tools.rand
import random

#获取数据
name = tools.rand.name()
account = tools.rand.phone_num()
saving = random.choice(range(10000,500000))

#连接数据库
conn = pymysql.connect(
	host = '127.0.0.1',
	port = 3306,
	user = 'root',
	passwd = '952411',
	db = 'python',
	charset = 'utf8'
)

#获取游标
cursor = conn.cursor()

#插入数据
sql = "insert into trade (name,account,saving) values ('%s','%s',%.2f)"
data = (name,account,saving)
cursor.execute(sql % data)
conn.commit()
print('成功插入',cursor.rowcount,'条数据')

#查询数据
sql = "select * from trade"
# data = ('13775736752')
cursor.execute(sql)
for row in cursor.fetchall():
    print("ID:%d\tName:%s\taccount:%s\tSaving:%.2f\tExpend:%.2f\tincome:%.2f" % row)
print('共查找出', cursor.rowcount, '条数据')

# 关闭连接
cursor.close()
conn.close()