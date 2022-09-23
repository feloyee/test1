import pymysql

# 连接数据库
db = pymysql.connect(host="localhost", port=3322, user="root", password="sh23036036", db="testdb")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000.0)"""

try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果出错则对数据库进行回滚
    db.rollback()

# 关闭数据库连接
db.close()