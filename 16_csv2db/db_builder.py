# Sports! - Sean Ging and Deven Maheshwari
# SoftDev
# K16 - All About Databse/Skeleton stub/SQLITE3 BASICS
# Oct 21 2021 


import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) # open if file exists, otherwise create
c = db.cursor()               # facilitate db ops -- you will use cursor to trigger db events
courses_dict = {}             # dictonary for courses.csv

#==========================================================

command = "CREATE TABLE courses(code TEXT, mark INTEGER, id INTEGER);"          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

# < < < INSERT YOUR TEAM'S POPULATE-THE-DB CODE HERE > > >
with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        code = row['code']
        mark = row['mark']
        id = row['id']
        courses_dict[code] = [mark, id]

for keys in courses_dict: 
    command = 'INSERT INTO courses VALUES (?, ?, ?);'
    params = (keys, courses_dict[keys][0], courses_dict[keys][1])
    c.execute(command, params)   




#==========================================================

db.commit() #save changes
db.close()  #close database


