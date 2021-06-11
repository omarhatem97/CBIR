from db import *
import os 
from FeatureExtractor import *
import pickle
import cv2
from Evaluation import *
from natsort import natsorted

image_path = r'./multimedia dataset'
# image_path = r'./multi_images'
# image_path = r'C:/Users/reemn/Downloads/copydays_original'


database = DB("cbDatabase")

# database = DB()
# database.createDataBase()  #call it just once

mycursor = database.get_cursor()
# mycursor.execute("DROP DATABASE cbDatabase")

# mycursor.execute("DROP TABLE ImagesDB")
# mycursor.execute("SHOW TABLES")

# for x in mycursor:
#   print(x)



mycursor.execute("CREATE TABLE ImagesDB (id INT AUTO_INCREMENT PRIMARY KEY, Histogram BLOB, ColorLayout LONGBLOB ,MeanColor BLOB ,MeanColor2 BLOB , Path VARCHAR(256))")
# mycursor.execute("CREATE TABLE ImagesDB (id INT AUTO_INCREMENT PRIMARY KEY, Histogram BLOB, ColorLayout BLOB ,MeanColor BLOB , Path VARCHAR(256))")

i = 1
for imagefile in natsorted(os.listdir(image_path)): #loop on images for the 1st time to be saved in database
    print(imagefile)
    image =  cv2.imread(image_path+str('/')+imagefile)     
    a = FeatureExtractor(image)  
    c = a.ColorLayout()   # save features in database
    d = a.Histogram()
    e = a.mean_color()
    f = a.unique_count_app()
    color =pickle.dumps(c)
    hist = pickle.dumps(d)
    mean = pickle.dumps(e)
    mean2 = pickle.dumps(f)
    #print(type(hist))
    # mycursor.execute("INSERT INTO ImagesDB (id,Histogram,ColorLayout,MeanColor, Path) VALUES(%s,%s,%s,%s,%s)", (i,hist,color,mean,image_path+str('/')+imagefile))
    mycursor.execute("INSERT INTO ImagesDB (id,Histogram,ColorLayout,MeanColor,MeanColor2,Path) VALUES(%s,%s,%s,%s,%s,%s)", (i,hist,color,mean,mean2,image_path+str('/')+imagefile))
    # mycursor.execute("INSERT INTO ImagesDB (id,Histogram,MeanColor,MeanColor2,Path) VALUES(%s,%s,%s,%s,%s)", (i,hist,mean,mean2,image_path+str('/')+imagefile))
    i=i+1
    
######################################
image =  cv2.imread(r'./multimedia dataset/142.jpg')     
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
i=1  
# print(result[0][0])
for pic in result:
  arr = pickle.loads(pic[0])
  error = obj.HistogramNormalizedDifference(c,arr,cv2.imread(pic[1]))
  print(i)
  # print(error)
  i+=1
  if error >= 0.1:
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

