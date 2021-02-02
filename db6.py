from sqlite3 import *

con = None
try:
	con = connect("Mini_project.db")
	print("connected")
	cursor = con.cursor()
	sql = "select * from student"
	cursor.execute(sql)
	data = cursor.fetchone()
	while data:
		print(data)
		print("rno = ", data[0], "names = ", data[1], "marks = ", data[2])
		data = cursor.fetchone()
except Exception as e:
	print("selection issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")