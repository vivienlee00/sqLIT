#Vivien Lee
#SoftDev1 pd7
#HW9 -- No Treble
#2017-10-15

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


dbfile = "hw9.db"

db = sqlite3.connect(dbfile) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#create a separate sqlite3 table for each csv file
c.execute("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")

#initialize DictReader for each csv file
peeps_reader = csv.DictReader(open("peeps.csv"))
courses_reader = csv.DictReader(open("courses.csv"))

#insert values from csv file into sqlite3 table
for row in peeps_reader:
    print(row)
    c.execute("INSERT INTO peeps VALUES (\""+row['name']+"\","+row['age']+","+row['id']+")")

for row in courses_reader:
    print(row)
    c.execute("INSERT INTO courses VALUES (\""+row['code']+"\","+row['mark']+","+row['id']+")")

db.commit() #save changes
db.close()  #close database
