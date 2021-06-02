import mysql.connector


def convertArrToStr(l):
    """
        convert array to string, to be able to store it in database
    """
    listToStr = ','.join([str(elem) for elem in l])
    return listToStr





mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="cbDatabase"
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
# mycursor.execute("CREATE TABLE customers2 (id INT PRIMARY KEY AUTO_INCREMENT,name VARCHAR(255), address VARCHAR(255) DEFAULT 'Sandnes' )")

sql = "INSERT INTO customers2 (name) VALUES (%s)"
val = ("shi")

mycursor.execute(sql, val)

mydb.commit()

mycursor.execute("SELECT * FROM customers2")

for i in mycursor:
    print(i)


# print("1 record inserted, ID:", mycursor.lastrowid)



