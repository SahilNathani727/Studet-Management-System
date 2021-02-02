from sqlite3 import *

con = None
try:
	con = connect("Mini_project.db")
	print("connected")
	cursor = con.cursor()
	sql = "update student set name = '%s', marks = '%d' where rno = '%r'"
	rno = int(input("enter rno to update "))
	name = input("enter new name ")
	marks = int(input("enter marks "))
	args = (name, rno, marks)
	cursor.execute(sql %args)
	if cursor.rowcount >= 1:
		con.commit()
		print("record update")
	else:
		print(rno ,"does not exists ")

except Exception as e:
	con.rollback()
	print("record updation issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")