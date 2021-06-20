import sqlite3

#STEP 1: CREATE (DATABASE
def create_table():
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTERGER, price REAL)")
  conn.commit()
  conn.close

#STEP 4: COMMIT CHANGES TO THE DATABASE
def insert(item,quantity,price):
  conn=sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
  conn.commit()
  conn.close

insert("Coffee Cup", 10, 5)

#VIEW
def view():
  conn = sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("SELECT * FROM store")
  rows=cur.fetchall()
  conn.close()
  return rows

#DELETE
def delete(item):
  conn = sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("DELETE FROM store WHERE item=?",(item,))
  rows=cur.fetchall()
  conn.close()
  

#UPDATE
def update(quantity, price, item):
  conn = sqlite3.connect("lite.db")
  cur=conn.cursor()
  cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity, price, item))
  rows=cur.fetchall()
  conn.close()

#update(11,6,"Wine Glass")
#delete("Wine Glass")
print(view())















#SIMPLE SQLITE EXAMPLE
""" 
import sqlite3

#STEP 1: CONNECT TO A DATABASE
conn=sqlite3.connect("lite.db")
#STEP 2: CREATE A CURSOR OBJECT
cur=conn.cursor()
#STEP 3: WRITE AN SQL QUERY - create and table are keywords and store is the name
cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INTERGER, price REAL)")
cur.execute("INSERT INTO store VALUES('Wine Glass',8,10.5)")
#STEP 4: COMMIT CHANGES TO THE DATABASE
conn.commit()
conn.close """