import psycopg2

#STEP 1: CREATE (DATABASE
def create_table():
  conn=psycopg2.connect("dbname='database1' user='postgres' password='postpass18' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS store(item TEXT, quantity INT, price REAL)")
  conn.commit()
  conn.close

#STEP 4: COMMIT CHANGES TO THE DATABASE
def insert(item,quantity,price):
  conn=psycopg2.connect("dbname='database1' user='postgres' password='postpass18' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
  conn.commit()
  conn.close


#VIEW
def view():
  conn = psycopg2.connect("dbname='database1' user='postgres' password='postpass18' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("SELECT * FROM store")
  rows=cur.fetchall()
  conn.close()
  return rows

#DELETE
def delete(item):
  conn = psycopg2.connect("dbname='database1' user='postgres' password='postpass18' host='localhost' port='5432'")
  cur=conn.cursor()
  cur.execute("DELETE FROM store WHERE item=%s",(item,))
  rows=cur.fetchall()
  conn.close()
  

#UPDATE
def update(quantity, price, item):
  conn = psycopg2.connect("lite.db")
  cur=conn.cursor()
  cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",(quantity, price, item))
  rows=cur.fetchall()
  conn.close()


create_table()
insert("orange", 10, 5)
insert("banana", 5, 2.5)
#update(20,15,0,"apple")
#delete("Orange")
print(view())













