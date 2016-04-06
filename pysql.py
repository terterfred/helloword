import pymysql
db = pymysql.connect(host="localhost", user="Fred", passwd="1111", db="test")
cur = db.cursor()
# sql = "INSERT INTO test (email, description) VALUES (%s, %s)"
# cur.execute(sql,("tliu13@utexas.edu", "secret"))

cur.execute("SELECT * FROM test")
result = cur.fetchone()
print (result)

