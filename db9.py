from sqlite3 import *

con = None
try:
	con = connect("Miniproject.db")
	print("connected")
	cursor = con.cursor()
	sql = "drop table student"
	cursor.execute(sql)
except Exception as e:
	con.rollback()
	print("drop issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")