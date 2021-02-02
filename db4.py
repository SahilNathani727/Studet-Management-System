from sqlite3 import *

con = None
try:
	con = connect("Mini_project.db")
	print("connected")
	cursor = con.cursor()
	sql = "insert into student values('%r', '%s', '%d')"
	rno = int(input("enter rno "))
	name = input("enter name ")
	marks = int(input("enter marks: "))
	args = (rno, name, marks)
	cursor.execute(sql %args)
	con.commit()
	print(cursor.rowcount)
	print("record created")

except Exception as e:
	con.rollback()
	print("record creation issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")