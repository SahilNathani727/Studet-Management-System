from sqlite3 import *

con = None
try:
	con = connect("Mini_project.db")
	print("connected")
	cursor = con.cursor()
	sql = "create table student(rno int primary key not null, name text, marks int)"
	cursor.execute(sql)
	print("table created")

except Exception as e:
	print("table creation issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")