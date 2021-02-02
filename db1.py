from sqlite3 import *

con = None
try:
	con = connect("Mini_project.db")
	print("connected")
except Exception as e:
	print("conn issue ", e)
finally:
	if con is not None:
		con.close()
		print("closed")