#!/usr/bin/python3

import sys
import MySQLdb
db = MySQLdb.connect(host='localhost', user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
cur = db.cursor()
cur.execute("SELECT * FROM states")
rows = cur.fetchall()

for row in rows:
    print(row)
