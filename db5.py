from sqlite3 import *

con = None
try:
	con = connect("Mini_project.db")
	print("connected")
	cursor = con.cursor()
	sql = "select * from student"
	cursor.execute(sql)
	data = cursor.fetchall()
	print(data)		# list of tuples
	for d in data:
		print("rno = ", d[0], "names = ", d[1], "marks = d[2]")
except Exception as e:
	print("selection issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")