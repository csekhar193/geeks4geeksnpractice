import MySQLdb

db=MySQLdb.connect('localhost','root','w433iqoq','TESTDB')

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print "Database version : %s" % data

db.close()