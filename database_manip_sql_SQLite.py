#  Python sqlite progam to CREATE , INSERT AND UPDATE RECORDS.

import sqlite3 #import sqlite library
db = sqlite3.connect('C:/Users/User/Dropbox/KR22100004527/Data Science Bootcamp/T38/data/student_db') #connecting to the database student_db
cursor = db.cursor() #Get a cursor object

cursor.execute( '''  CREATE TABLE python_programming (id integer PRIMARY KEY, name text, grade integer)  ''' ) #cursor to execute CREATE statement
db.commit()             
print('Table Created')

cursor = db.cursor() #Get a cursor object

# Assigning the data to variable to be inserted all at a time.

id1    = 55
name1 = 'Carl Davis'
grade1 = 61

id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

id3 = 77
name3 = 'Jane Richards'
grade3 = 78

id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45

id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

students_ = [(id1,name1,grade1),(id2,name2,grade2),(id3,name3,grade3),(id4,name4,grade4),(id5,name5,grade5)]

#Inserting all records using executemany funcion
cursor.executemany(''' INSERT INTO python_programming (id,name,grade) values(?,?,?)''',students_)
print('Records Inserted') #Display messages
db.commit()   #Commit the records inserted

cursor = db.cursor() #Get a cursor object

grade = 60 , 80 #Assigning the values to be passed in cursor

cursor.execute(''' SELECT * FROM python_programming WHERE grade BETWEEN ? and ? ''',(grade))

db.commit() #commit the execution

#Display all records with grade between 60 and 80
print(f'All records with grade between 60 AND 80 ')
cursor.execute('''SELECT * FROM python_programming WHERE grade BETWEEN ? and ? ''',(grade))
for row in cursor:
    print('{0} ,{1} ,{2}'.format(row[0], row[1], row[2]))

cursore = db.cursor() #Get a cursor object

#Change the grade for below assigned name
grade = 65
name = 'Carl Davis'
cursor.execute(''' UPDATE python_programming SET  grade = ? WHERE name = ? ''',(grade,name,))
print(f'{name} grade Changed to {grade}.') #Display the message

db.commit()

cursor = db.cursor() #Get a cursor object

#Delete the record 
name = 'Dennis Fredrickson'
cursor.execute(''' DELETE FROM python_programming WHERE name = ? ''',(name,)) #Execute cursor to delete the record
print(f'{name} record is deleted.')

db.commit()

#Changed the grade of all people to 90 with an id less than 55
cursor = db.cursor() #Get a cursor object
id = 55
grade = 90
cursor.execute(''' UPDATE python_programming SET GRADE = ? WHERE id < ? ''',(grade,id,))

print(f'Changed the grade of all people with an id less than {id}.')

db.commit()

#Display the final structure of the table.
print('SELECT id,name, grade FROM python_programming:')
cursor.execute('''SELECT id,name, grade FROM python_programming''')
for row in cursor:
    print('{0} ,{1} , {2}'.format(row[0], row[1], row[2]))

#Drop the table
cursor.execute('''DROP TABLE python_programming''')
print('python_programming table deleted.')

db.commit()
db.close()      #Close the connection
print('Connection to database closed')