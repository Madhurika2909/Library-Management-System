import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Nar456trof",
  database="11A1"
)
mycursor = mydb.cursor()

# Print the database in a tabulated form
def PrintFun():
  opt = input("Order by: 1: Admno,2: Name,3: Class, 4: DOB, 5: Marks ? ")
  OrderItems = ['Admno','Name','Class','DOB','Marks']
  sql = "select *from students order by " + OrderItems[opt-1] + " ASC"
  mycursor.execute(sql)
  myresult = mycursor.fetchall()
  for des in mycursor.description:
    print(des)
 
  widths = [10,20,5,5,10,5]
  columns = []
  tavnit = '|'
  separator = '+' 
  
  for cd in mycursor.description:
      columns.append(cd[0])
  
  for w in widths:
      tavnit += " %-"+"%ss |" % (w,)
      separator += '-'*w + '--+'
  
  print(separator)
  print(tavnit % tuple(columns))
  print(separator)
  for row in myresult:
    #print('{0[0]:10d} | {0[1]:20s} | {0[2]:5d} | {0[3]:5s} | {0[4]:} | {0[5]:5d}'.format(res))
    print(tavnit % row)
  print(separator)

# Print all databases.
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x) 

mycursor.execute("use MyLib")
mycursor.execute("DROP table MyBooks")
#mycursor.execute("CREATE TABLE Books(SNo int(3),CodeNo int(5),Name char(40),Type char(20))")
sql = "CREATE TABLE MyBooks (IDNo integer primary key,name VARCHAR(255), address VARCHAR(255))"
rows_count = mycursor.execute(sql)
print(rows_count)
if rows_count > 0:
  myresult = mycursor.fetchall()
  print(myresult)     
sql = "INSERT INTO MyBooks (IDNo,name,address) VALUES (%s, %s, %s)"
val = [
  (1,'Peter', 'Lowstreet 4'),
    (2,'Amy', 'Apple st 652'),
    (3,'Hannah', 'Mountain 21'),
    (4,'Michael', 'Valley 345'),
    (5,'Sandy', 'Ocean blvd 2'),
    (6,'Betty', 'Green Grass 1'),
    (7,'Richard', 'Sky st 331'),
    (8,'Susan', 'One way 98'),
    (9,'Vicky', 'Yellow Garden 2'),
    (10,'Ben', 'Park Lane 38'),
    (11,'William', 'Central st 954'),
    (12,'Chuck', 'Main Road 989'),
    (13,'Viola', 'Sideway 1633')
]
sql = "INSERT INTO MyBooks values(101,'harry potter and the philosopher stone','Fiction')"
rows_count = mycursor.execute(sql)
#rows_count = mycursor.executemany(sql,val)
if rows_count > 0:
  myresult = mycursor.fetchall()
print(rows_count)
  
PrintFun()
mycursor.execute("Update students set name = 'tendy' WHERE name ='wendy'")
mycursor.execute("insert into students values(11610,'vijaya',12,'A1','1976-04-04',89)")
PrintFun()
