import MySQLdb as dbapi
import sys
import csv

QUERY='SELECT * FROM mydb.people;'
database=dbapi.connect(host='localhost',user='root',passwd='password')

cur=database.cursor()
cur.execute(QUERY)
result=cur.fetchall()

c = csv.writer(open('dumpcsv.csv', 'w'))
for x in result:
    c.writerow(x)
