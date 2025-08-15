import pycopg2 
import os,sys 
# create connection
cnn = None
cnn = psycopg2.connect(databse = "name",user = "user",password = 'pass',host = "localhost",port = 5342)
#create cursor
cur = cnn.cursor()
cur.execute('''create table employee(emp_num int primary key,emp name varchar(40))''')
#commit
cnn.commit()
#close currsor
cur.close()
# connection close
cnn.close