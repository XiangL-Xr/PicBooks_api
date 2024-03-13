import pymysql

## 建立连接
db = pymysql.connect(
    "localhost",
    "lixiang",
    "lixiang",
    "books_table"
)

## 获取游标
m_cur = db.cursor()
sql = "select * from blogs"
try:
    m_cur.execute(sql)
    results = m_cur.fetchall()
    print("id", "user_id", "name")
    # 遍历结果
    for row in results:
        id = row[0]
        user_id = row[1]
        name = row[4]
        print(id, user_id, name)

except Exception as e:
    raise e

finally:
    db.close()