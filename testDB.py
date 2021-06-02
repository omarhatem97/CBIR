from mysql.connector.utils import intstore
from db import *


database = DB("cbDatabase")

cursor = database.cursor

# cursor.execute("CREATE TABLE images(\
#                     id INT PRIMARY_KEY AUTO_INCREMENT,\
#                     f_histogram NVARCHAR(1000000000),\
#                     f_colorLayout NVARCHAR(1000000000),\
#                     f_meanColor NVARCHAR(1000000000),\
#                     url VARCHAR(4))")

# cursor.execute("CREATE TABLE images(id INT PRIMARY KEY AUTO_INCREMENT,f_histogram TEXT(1000000),f_colorLayout TEXT(1000000),f_meanColor TEXT(1000000),url VARCHAR(4))") 

database.insert_to_images('f4', 'f5', 'f6', '1')

database.printTable('images')




# database.createDataBase()  #call it just once

# cursor = database.get_cursor

# create a table
# database.createTable("test2")
# database.insert('test2', [1, 2, 3])
# database.insert('test2', [4, 5, 6])
# database.insert('test2', [7, 8, 9])

# database.createTable("test4")
# cursor = database.get_cursor()

# sql = "INSERT INTO test4 (arr) VALUES (%s)"
# val = ("omar")
# cursor.execute(sql, val)
# database.get_db().commit()


# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")

# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")



# database.printTable("testArray")






