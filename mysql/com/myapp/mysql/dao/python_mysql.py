#author guojingyu
#date      Sep 18, 2014
import MySQLdb
conn = MySQLdb.connect(host='localhost',user='root',passwd='root',db='mydb')
cursor = conn.cursor()
sql = "select * from jobs_job;"
cursor.execute(sql)
#jobs = cursor.fetchone()
#jobs = cursor.fetchmany(3)
jobs = cursor.fetchall()
print jobs
cursor.close()
conn.close()

'''
http://mysql-python.sourceforge.net/MySQLdb-1.2.2/public/MySQLdb.cursors.Cursor-class.html
'''
