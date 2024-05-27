#Python Program for bookstore clerk
import sqlite3        #import sqlite library
db = sqlite3.connect('ebookstore')    #Create a database
cursor = db.cursor() # Get a cursor object
print("Connection Established")
cursor.execute('''DROP TABLE  IF EXISTS books ''')
#Create table books
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS books (id INTERGER PRIMARY KEY , Title VARCHAR(255) , Author VARCHAR(255) ,Qty INTEGER)
''')
print('Table Created')
db.commit()

#Insert records into tables
cursor = db.cursor()
id1    = 3001
Title1 = 'A Tale of Two Cities'
Author1 = 'Charles Dickens'
Qty1 = 30

id2    = 3002
Title2 = 'Harry Potter and the Philosopher''s Stone'
Author2 = 'J.K.Rowling'
Qty2 = 40

id3   = 3003
Title3 =  'The Lion,the Witch and the Wardrobe'
Author3 = 'C.S.Lewis'
Qty3 = 25

id4   = 3004
Title4 = 'The Lord of the Rings'
Author4 = 'J.R.R Tolkien'
Qty4 = 37

id5    = 3005
Title5 = 'Alice in Wonderland'
Author5 = 'Lewis Carroll'
Qty5 = 12

books_ = [(id1,Title1,Author1,Qty1),(id2,Title2,Author2,Qty2),
(id3,Title3,Author3,Qty3),(id4,Title4,Author4,Qty4),
(id5,Title5,Author5,Qty5)]

#Inserting all records using executemany funcion
cursor.executemany(''' INSERT INTO books (id,Title,Author,Qty) values(?,?,?,?)''',books_)
print('Records Inserted') #Display messages
db.commit()

#Displaying the records 
cursor = db.cursor()
cursor.execute(''' Select id,Title,Author,Qty from books ''')
for row in cursor:
    print('{0},{1},{2},{3}'.format(row[0],row[1],row[2],row[3]))
db.commit()    
while True:
#Menu option for user
    Menu = int(input (''' Please enter the following option from menu :
            1.Enter book
            2.Update book
            3.Delete book
            4.Search book
            0.Exit          
        : '''))
    ## Option 1 : Enter the book          
    if Menu == 1   :
        #Request user the details of the books to be added
        id = int(input('Enter id :'))       
        Title = input ('Enter the title of the book :')
        Author = input('Enter the Author of the book :')
        Qty = int(input('Enter Quantity :'))

        cursor = db.cursor()
        cursor.execute (''' INSERT INTO books values (?,?,?,?) ''',(id,Title,Author,Qty,))  #Adding the new books to table
        opt = input('Would to like to view the book entered now (y/n):').lower() #Request user view option
        if opt == 'y':
            cursor.execute(''' SELECT id,Title,Author,Qty FROM books WHERE id = ? ''',(id,)) #Viewing the book added
            for row in cursor:
                print('{0},{1},{2},{3}'.format(row[0],row[1],row[2],row[3]))
        else :   
            print("Book Entered!")
        db.commit()
        continue
    elif Menu == 2 :
        #Request user to update the existing record
        cursor = db.cursor()
        id = int(input("Enter id :"))  
        upd = input ('What would you like to update (Title/Author/Qty) :').lower() 
        if upd == 'title': #Update  title
            ntitle = input('Enter the new title :')
            cursor.execute(''' UPDATE books SET Title = ? WHERE id = ?''',(ntitle,id,))
            print('Title Update!')
        elif upd == 'author': #Update the author
            nauthor = input("Enter the Author to update:") 
            cursor.execute(''' UPDATE books SET Author = ? WHERE id = ? ''',(nauthor,id,))   
            print('New Author Updated')
        elif upd == 'qty': #Update quantity
            nqty = int(input('Enter new Qty :'))
            cursor.execute(''' UPDATE books SET Qty = ? WHERE id = ? ''',(nqty,id,))        
            print('Quantity Updated')
        opt = input('Would to like to view the book updated now (y/n):').lower() #Request user view option
        if opt == 'y':
            cursor.execute(''' SELECT id,Title,Author,Qty FROM books WHERE id = ? ''',(id,)) #Viewing the book added
            for row in cursor:
                print('{0},{1},{2},{3}'.format(row[0],row[1],row[2],row[3]))
        else :   
            print("Book Updated!")    
        db.commit() 
        continue
    elif Menu == 3 :   # Delete the book from table.
        cursor = db.cursor()
        id = int(input("Enter id :"))
        cursor.execute(''' DELETE FROM books WHERE  id = ? ''',(id,))
        print('Book %d Deleted' %id)
        db.commit()
        continue
    elif Menu == 4 :  #Search the book
        id = int(input("Enter id :"))#Request the id of the book to search
        print(f'SELECT id,Title,Author,Qty FROM books WHERE id = {id}')
        cursor.execute(''' SELECT id,Title,Author,Qty FROM books WHERE id = ? ''',(id,))#searching the book requested
        for row in cursor:
                print('{0},{1},{2},{3}'.format(row[0],row[1],row[2],row[3]))
        continue        
    elif Menu == 0 : #Exit
        print ('Thank you ! Visit Again.')
        break

cursor.execute('''DROP TABLE books''') #drop table
print('books table deleted!')

db.commit()
db.close()
print('Connection to database closed')