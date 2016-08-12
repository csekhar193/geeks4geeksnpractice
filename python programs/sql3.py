import MySQLdb
db = MySQLdb.connect('localhost','root','w433iqoq','MVGR')
cursor = db.cursor()
sql = """ INSERT INTO Professor (First_name,Last_name,Age,Sex,degree)
		  VALUES ('ramana','reddy',40,'male','Phd'),
		  		 ('chandra','sekhar',35,'male','Mtech'),
		  		 ('suresh','kumar',33,'male','Mtech'),
		  		 ('satyanarayana','raju',32,'male','Mtech'),
		  		 ('nagendra','kumar',25,'male','Mtech')"""
try:
	cursor.execute(sql)
	db.commit()
except:
	db.rollback()
db.close()