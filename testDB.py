from db import *
import os 
from FeatureExtractor import *
import pickle

image_path = r'C:\Users\reemn\Downloads\copydays_original'
Histogram =[]

database = DB("cbDatabase")

# database = DB()
# database.createDataBase()  #call it just once

mycursor = database.get_cursor()
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)
mycursor.execute("DROP TABLE ImagesDB")


mycursor.execute("CREATE TABLE ImagesDB (id INT AUTO_INCREMENT PRIMARY KEY, Histogram BLOB, ColorLayout TEXT ,MeanColor TEXT , Path VARCHAR(256))")

# i = 1
for imagefile in os.listdir(image_path): #loop on images for the 1st time to be saved in database
    
    image =  cv2.imread(image_path+str('/')+imagefile)     
    a = FeatureExtractor(image)  
    c = a.Histogram()   # save features in database
 
    hist =pickle.dumps(c)
    print(type(hist))
    mycursor.execute("INSERT INTO ImagesDB (Histogram) VALUES(%s)", ( hist ))

    # hist= " "
    # hist.join(c)
    # # print(hist)
    # sql = "INSERT INTO ImagesDB (id, Histogram) VALUES (%s, %s)"
    # val = ( id , hist)
    # mycursor.execute(sql, val)
    # database.commit()
    # i=i+1

print(mycursor.rowcount, "record inserted.")    
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# cursor = database.get_cursor()

# create a table





