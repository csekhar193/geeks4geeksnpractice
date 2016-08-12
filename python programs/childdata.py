import MySQLdb
db = MySQLdb.connect('localhost','root','w433iqoq','MVGR')
cursor = db.cursor()
sql = """ INSERT INTO Student (First_name,Last_name,Age,Sex)
		  VALUES ('kiran','usk',21,'male'),
		  		 ('shantu','a',20,'male')"""
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()