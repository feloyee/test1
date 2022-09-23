import pymysql

# 连接数据库
db = pymysql.connect(host="localhost", port=3322, user="root", password="sh23036036", db="testdb")

# 创建游标
cursor = db.cursor()

# 游标执行方法
cursor.execute("select version()")

# 执行游标方法后赋值给变量
data = cursor.fetchone()

# 打印变量内容
print("Database version: %s" % data)

# 关闭游标
db.close()

