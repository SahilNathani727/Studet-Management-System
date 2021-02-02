from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import requests
import socket
import bs4
import matplotlib.pyplot as plt
import numpy as np

class invalidrno(Exception):
	def __init__(self,msg):
		self.msg = msg
class invalidname(Exception):
	def __init__(self,msg):
		self.msg = msg
class invalidmarks(Exception):
	def __init__(self,msg):
		self.msg = msg

def f1():
	root.withdraw()
	adst.deiconify()
	adst_entRno.delete(0, END)
	adst_entName.delete(0, END)
	adst_entRno.focus()
def f2():
	adst.withdraw()
	root.deiconify()

def f3():
	root.withdraw()
	vist.deiconify()
	vist_stdata.delete(1.0, END)
	con = None
	try:
		con = connect("Mini_project.db")
		cursor = con.cursor()
		sql = "select * from student";
		cursor.execute(sql)
		data = cursor.fetchone()
		info=""
		for d in data:
			info = info + "rno = " + str(d[0]) + " Name = " + str(d[1]) + " Marks = " + str(d[2])
		vist_stdata.insert(INSERT, info)
	except Exception as e:
		showerror("failure ", e)
		con.rollback()
def f4():
	vist.withdraw()
	root.deiconify()
def f5():
	root.withdraw()
	updt.deiconify()
	upst_entEnterRno.delete(0,END)
	upst_entEnterName.delete(0,END)
	upst_entEnterMarks.delete(0,END)
	upst_entEnterRno.focus()
def f6():
	updt.withdraw()
	root.deiconify()	
def f7():
	root.withdraw()
	dlt.deiconify()
	delst_entEnterRno.delete(0,END)
	delst_entEnterRno.focus()
def f8():
	dlt.withdraw()
	root.deiconify()
def save():
	con = None
	try:
		con = connect("Mini_project.db")
		cursor = con.cursor()
		rno = adst_entRno.get()
		name = adst_entName.get()
		marks = adst_entMarks.get()
		if rno == "":
			raise invalidrno("rno should be +ve Integer")
		try:
			rno=int(rno)
		except Exception as e:
				raise invalidrno("rno should be Integer")
		if rno<0:
			raise invalidrno('Rno should not be -ve.')
		
		if name == "" or len(name)<2 :
			raise invalidname("Name Should not be at least two letters ")
		if not name.isalpha() :
			raise invalidname("Name should contain only alphabets ")
		if marks == "":
			raise invalidmarks("Marks should not be empty ")
		try:
			marks=int(marks)
		except Exception as e:
			raise invalidmarks("Marks should be integer value.")
		if marks<0 or marks>100:
			raise invalidmarks('Marks out of range(0-100).')
		sql="create table if not exists student(rno int primary key,name text not null,marks int not null)"
		cursor.execute(sql)
		sql="insert into student values('%r','%s','%d')"
		args = (rno, name, marks)
		cursor.execute(sql %args)
		con.commit()
		showinfo("Result", "record inserted")
	except IntegrityError as e:
		con.rollback()
		showerror("Error","Record already exists.")
	except Exception as e:
		showerror("failure ", e)
		con.rollback()
	finally:
		if con is not None:
			con.close()

def update():
	con = None
	try:
		con = connect("Mini_project.db")
		cursor = con.cursor()
		rno = updt_entRno.get()
		name = updt_entName.get()
		marks = updt_entMarks.get()
		if rno=="" :
			raise InvalidRollNo("Rno should not be empty.")
		try:
			rno=int(rno)
		except Exception as e:
			raise invalidrnoo("Rno should be integer value.")
		if rno<0:
			raise invalidrno('Rno should not be -ve.')
		
		if name=="" or len(name)<2 :
			raise invalidname("Name should be of at least 2 letters.")
		if not name.isalpha():
			raise invalidname("Name should contain alphabets only.")

		if marks=="" :
			raise invalidmarks("Marks should not be empty.")
		try:
			marks=int(marks)
		except Exception as e:
			raise invalidmarks("Marks should be integer value.")
		if marks<0 or marks>100:
			raise invalidmarks('Marks out of range(0-100).')

		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
			if rno in d:
				sql="update student set name='%s',marks='%d' where rno='%r'"
				args=(name,marks,rno)
				cursor.execute(sql %args)
				con.commit()				
				showinfo("Message","Record updated")
				break
		else:
			con.rollback()
			msg=str(rno)+" rno doesn't exist"
			showerror("Error",msg)
	except Exception as e:
		con.rollback()
		showerror("Issue : ",e)
	finally:
		if con is not None:
			con.close()


	
def delete():
	con = None
	try:
		con = connect("Mini_project.db")
		print("connected")
		cursor = con.cursor()
		sql = "delete from student where rno = '%r'"
		rno = int(dlt_entRno.get())
		args = (rno)
		cursor.execute(sql %args)
		if cursor.rowcount >= 1:
			con.commit()
			showinfo("record deleted", "Deleted")
		else:
			showinfo(rno ,"does not exists ")	

	except Exception as e:
		con.rollback()
		showerror("record deletion issue ", e)

def charts():
	student_names=[]
	student_marks=[]
	con = None
	try:
		con = connect("Mini_project.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			student_names.append(d[1])
			student_marks.append(d[2])
		x=np.arange(len(student_names))
		plt.bar(x,student_marks,color=['yellow','red','blue'])
		plt.xticks(x,student_names)
		plt.title("Batch Information")
		plt.xlabel("Students")
		plt.ylabel("Marks")
		plt.show()
	except Exception as e:
		showerror("Issue :" , e)
	
root = Tk()
root.title("S.M.S")
root.geometry("500x500+400+100")


addbtn = Button(root, text="Add",font=('arial',18,'bold'),height=1,width=10,command=f1)
viewbtn = Button(root, text="View",font=('arial',18,'bold'),width=10,command=f3)
updatebtn = Button(root,text="Update",font=('arial',18,'bold'),width=10,command=f5)
dltbtn= Button(root,text="Delete",font=('arial',18,'bold'),width=10,command=f7)
chartsbtn = Button(root,text="Charts",font=('arial',18,'bold'),width=10,command=charts)
lbllctn = Label(root,text="Location:",font=('arial',15,'bold'))
lbltemp = Label(root,text="Temp:",font=('arial',15,'bold'))
lblqotd = Label(root,text="QOTD:",font=('arial',15,'bold'))
lblltn = Label(root,text=" ",font=('arial',15,'bold'))
lbltmp = Label(root,text=" ",font=('arial',15,'bold'))
lblqtd = Label(root,text=" ",font=('arial',15,'bold'))




try:
	socket.create_connection(("www.google.com", 80))
	res1 = requests.get("https://ipinfo.io")	
	data1 = res1.json()
	#city = data1['city']
	city = 'Akola'
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city 
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address =  a1 + a2  + a3 		
	res = requests.get(api_address)
	data = res.json()

	#coord = data['coord']
	#lon = coord['lon']
	#lat = coord['lat']
	lblltn.configure(text=" "+city)
	
	main = data['main']
	temp = main['temp']
	lbltmp.configure(text="" + str(temp))

	res2 = requests.get("https://www.brainyquote.com/quote_of_the_day")
	soup = bs4.BeautifulSoup(res2.text, "lxml")
	data2 = soup.find("img", {"class": "p-qotd"})

	quote = data2['alt']
	lblqtd.configure(text=quote[:28]+"\n"+quote[28:90]+"\n"+quote[90:140])
except OSError as e:
	print("issue ", e)

addbtn.pack(pady=5)
viewbtn.pack(pady=5)
updatebtn.pack(pady=5)
dltbtn.pack(pady=5)
chartsbtn.pack(pady=5)
lbllctn.place(x=10,y=325)
lbltemp.place(x=360,y=325)
lblqotd.place(x=10,y=375)
lblltn.place(x=130,y=325)
lbltmp.place(x=430,y=326)
lblqtd.place(x=130,y=375)


adst = Toplevel(root)
adst.title("Add St")
adst.geometry("500x500+400+100")


adst_lblRno=Label(adst,text="enter rno:",font=('arial',18,'bold'),)
adst_entRno=Entry(adst,bd=5,font=('arial',18,'bold'),width=20)
adst_lblName=Label(adst,text="enter name:",font=('arial',18,'bold'))
adst_entName=Entry(adst,bd=5,font=('arial',18,'bold'),width=20)
adst_lblMarks=Label(adst,text="enter marks:",font=('arial',18,'bold'))
adst_entMarks=Entry(adst,bd=5,font=('arial',18,'bold'),width=20)
adst_btnSave=Button(adst,text="Save",font=('arial',18,'bold'),command = save)
adst_btnBack=Button(adst,text="Back",font=('arial',18,'bold'),command=f2)


adst_lblRno.pack(pady=5)
adst_entRno.pack(pady=5)
adst_lblName.pack(pady=5)
adst_entName.pack(pady=5)
adst_lblMarks.pack(pady=5)
adst_entMarks.pack(pady=5)
adst_btnSave.pack(pady=5)
adst_btnBack.pack(pady=5)
adst.withdraw()






vist=Toplevel(root)
vist.title("View st")
vist.geometry("500x400+400+200")



vist_stdata = ScrolledText(vist, width=30, height=4, font = ('arial', 20, 'bold'))
vist_btnBack = Button(vist, text="Back",font = ('arial', 20, 'bold'),command=f4)


vist_stdata.pack(pady=10)
vist_btnBack.pack(pady=10)
vist.withdraw()






















updt = Toplevel(root)
updt.title("Update St.")
updt.geometry("500x500+400+100")


updt_lblRno=Label(updt,text="enter rno:",font=('arial',18,'bold'),)
updt_entRno=Entry(updt,bd=5,font=('arial',18,'bold'),width=20)
updt_lblName=Label(updt,text="enter name:",font=('arial',18,'bold'))
updt_entName=Entry(updt,bd=5,font=('arial',18,'bold'),width=20)
updt_lblMarks=Label(updt,text="enter marks:",font=('arial',18,'bold'))
updt_entMarks=Entry(updt,bd=5,font=('arial',18,'bold'),width=20)
updt_btnSave=Button(updt,text="Save",font=('arial',18,'bold'),command = update)
updt_btnBack=Button(updt,text="Back",font=('arial',18,'bold'),command=f6)


updt_lblRno.pack(pady=5)
updt_entRno.pack(pady=5)
updt_lblName.pack(pady=5)
updt_entName.pack(pady=5)
updt_lblMarks.pack(pady=5)
updt_entMarks.pack(pady=5)
updt_btnSave.pack(pady=5)
updt_btnBack.pack(pady=5)
updt.withdraw()







dlt = Toplevel(root)
dlt.title("Delete St.")
dlt.geometry("500x500+400+100")

dlt_lblRno=Label(dlt,text="enter rno:",font=('arial',18,'bold'))
dlt_entRno=Entry(dlt,bd=5,font=('arial',18,'bold'),width=20)
dlt_btnSave=Button(dlt,text="Save",font=('arial',18,'bold'),width=10,command=delete)
dlt_btnBack=Button(dlt,text="Back",font=('arial',18,'bold'),width=10,command=f8)

dlt_lblRno.pack(pady=5)
dlt_entRno.pack(pady=5)
dlt_btnSave.pack(pady=5)
dlt_btnBack.pack(pady=5)
dlt.withdraw()





















root.mainloop()