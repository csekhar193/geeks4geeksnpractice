import MySQLdb

db=MySQLdb.connect('localhost','root','w433iqoq','TESTDB')

cursor = db.cursor()

sql = """ INSERT INTO Employee(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
		  VALUES ('chanu','s',22,'M',2000),('chaitu','sekhar',22,'M',2000);"""

try:		  
	cursor.execute(sql)
	db.commit()
except ValueError:
	print "in exceptions", ValueError
db.close()