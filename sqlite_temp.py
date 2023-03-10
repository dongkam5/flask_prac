import sqlite3

conn =sqlite3.connect('database.db')
print('Opened database successfully')

conn.execute('CREATE TABLE STUDENTS (NAME TEXT, ADDR TEXT, CITY TEXT, PIN TEXT)')
print('Table created successfully')
conn.close()