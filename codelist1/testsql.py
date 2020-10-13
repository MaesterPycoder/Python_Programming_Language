# Importing Modules
import mysql.connector 

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "Sss@23052000",
    database = "pythonics"
	)
mycursor = mydb.cursor()
name = "Mr.Timber Lee"
emailid = "Lassan123@gmail.com"
dob = "25/89/56"
gender = "Male"
mobile = "+9189856"
password = "lee@123"
mycursor.execute(f"insert account_info values(2,'{name}','{emailid}','{dob}','{gender}','{mobile}','{password}')") 
mydb.commit()
mycursor.close()
mydb.close()


