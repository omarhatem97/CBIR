from db import *
import os 
from FeatureExtractor import *
import pickle
import cv2
from helpers.Evaluation import *
image_path = r'C:/Users/Lenovo/Pictures/MM'
Histogram =[]

database = DB("cbDatabase")

# database = DB()
# database.createDataBase()  #call it just once

mycursor = database.get_cursor()
# mycursor.execute("DROP DATABASE cbDatabase")
# mycursor.execute("SHOW DATABASES")

# for x in mycursor:
#   print(x)
#mycursor.execute("DROP TABLE ImagesDB")


# mycursor.execute("CREATE TABLE ImagesDB (id INT AUTO_INCREMENT PRIMARY KEY, Histogram BLOB, ColorLayout BLOB ,MeanColor BLOB , Path VARCHAR(256))")

# i = 1
# for imagefile in os.listdir(image_path): #loop on images for the 1st time to be saved in database
    
#     image =  cv2.imread(image_path+str('/')+imagefile)     
#     a = FeatureExtractor(image)  
#     c = a.ColorLayout()   # save features in database
#     d = a.Histogram()
#     e = a.mean_color()
#     color =pickle.dumps(c)
#     hist = pickle.dumps(d)
#     mean = pickle.dumps(e)
#     #print(type(hist))
#     mycursor.execute("INSERT INTO ImagesDB (id,Histogram,ColorLayout,MeanColor, Path) VALUES(%s,%s,%s,%s,%s)", (i,hist,color,mean,image_path+str('/')+imagefile))
#     i=i+1

image =  cv2.imread('C:/Users/Lenovo/Pictures/MM/200600.jpg')     
a = FeatureExtractor(image)  
c = a.Histogram() 

mycursor.execute("SELECT Histogram, Path FROM ImagesDB")

obj = Evaluation()
# fetch all the matching rows 
result = mycursor.fetchall()
# print(pickle.loads(result[0][1]))
# print(bytes(result[0][0],'utf-8'))

# for pin in result:
#   l = bytes(pin[0][0], 'utf-8')
#   arr=pickle.loads(l)
  
# print(result[0][0])
for pic in result:
  arr = pickle.loads(pic[0])
  error = obj.HistogramNormalizedDifference(c,arr,cv2.imread(pic[1]))
  print(error)
  if error >= 1e-4:
    print(pic[1])
  # error = obj.compare(c,arr)
  # if error<500:
  #   print(pic[1])
  # for pickledlist in pic[0][0]:
  #   arr = pickle.loads(pickledlist)
  #   error = obj.compare(c,arr)
  #   if error<100:
  #     print(pic[0][1])  

  


#     # hist= " "
#     # hist.join(c)
#     # # print(hist)
#     # sql = "INSERT INTO ImagesDB (id, Histogram) VALUES (%s, %s)"
#     # val = ( id , hist)
#     # mycursor.execute(sql, val)
#     # database.commit()
#     # i=i+1

# print(mycursor.rowcount, "record inserted.")    
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)

# mycursor.execute("SELECT * FROM ImagesDB")
  
# # fetch all the matching rows 
# result = mycursor.fetchall()
# print("rowcount ", mycursor.rowcount)

# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
# cursor = database.get_cursor()

# create a table