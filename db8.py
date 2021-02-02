from sqlite3 import *

con = None
try:
	con = connect("Mini_project.db")
	print("connected")
	cursor = con.cursor()
	sql = "delete from student where rno = '%r'"
	rno = int(input("enter rno to delete "))
	args = (rno)
	cursor.execute(sql %args)
	if cursor.rowcount >= 1:
		con.commit()
		print("record deleted")
	else:
		print(rno ,"does not exists ")

except Exception as e:
	con.rollback()
	print("record deletion issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")