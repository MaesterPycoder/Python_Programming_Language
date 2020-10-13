import mysql.connector
conn=mysql.connector.connect(
    user='root',
    password='Sss@23052000',
    host='127.0.0.1',
    database='shannu')
cur=conn.cursor()
name=input("Enter name=")
date=int(input("Enter date="))
sto=("insert into topics values(name='()',date='()'".format(name,date))
cur.execute(sto)
que=("select * from topics")
cur.execute(que)
for (name,date) in cur:
    print("(),()".format(name,date))
cur.close()
conn.commit()
conn.close()
