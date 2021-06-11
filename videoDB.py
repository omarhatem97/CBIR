from db import *
import codecs
import os 
import pickle
import cv2
from natsort import natsorted
from histogram import *


# video_path1 = r'./other/'
video_path = r'./videos/'
dir = r'./test/'
# database = DB()
# database.createDataBase()  #call it just once

database = DB("cbDatabase")

mycursor = database.get_cursor()


# mycursor.execute("CREATE TABLE VideosDB (id INT AUTO_INCREMENT PRIMARY KEY, B BLOB, G BLOB , R BLOB , Name VARCHAR(256) , Path VARCHAR(256))")

# i = 0
# recordings = os.listdir(video_path1)
# #print(recordings)
# for k in range(0,len(recordings)): #loop on videos for the 1st time to be saved in database
#     file = recordings[k]
#     histogram_generator1 = Histogram(video_path1,file)
#     b,g,r = histogram_generator1.generate_and_store_average_rgb_histogram()
#     b = pickle.dumps(b)
#     g = pickle.dumps(g)
#     r = pickle.dumps(r)
  
#     mycursor.execute("INSERT INTO VideosDB (B,G,R,Name,Path) VALUES(%s,%s,%s,%s,%s)", (b,g,r,file,video_path + file))




def test_video(dir,own):
  histogram_generator = Histogram(dir, own)
  b2,g2,r2 = histogram_generator.generate_and_store_average_rgb_histogram()
  mycursor.execute("SELECT B , G , R , Name , Path FROM VideosDB")
  results = mycursor.fetchall()
  return results,b2,g2,r2

def retrieve_video(results,b2,g2,r2):
    video_match = ""
    video_match_value = 0
    table_data = list()
    i = 0
    res = []
    for vid in results:
        arr = pickle.loads(vid[0])
        arr2= pickle.loads(vid[1])
        arr3 = pickle.loads(vid[2])
        arr4 = vid[3]
        histogram_generator1 = Histogram(dir, own)
        comparison = histogram_generator1.match(b2,g2,r2,arr,arr2,arr3)
        table_data.append([arr4, round(comparison, 5)])
        if i == 0:
          video_match = arr4
          video_match_value = comparison
        else:
            if comparison < video_match_value:
              video_match = arr4
              video_match_value = comparison
        i += 1
    sorted_res = sorted(table_data, key=lambda x: x[1])
    k = 0

    for i in sorted_res:
      if k == 5:
        break
      elif i[1] < 0.4:
          res.append(i)
      k = k+1
    if (len(res) == 0):
      res.append(sorted_res(0))
      
    return res, video_match


if __name__ == "__main__":
  recordings = ['good_fish.MP4','good_ear.mp4','airplane.mp4','bad_dog.MP4','beach.mp4','dog.mp4']
  own = recordings[0]
  results,b2,g2,r2 = test_video(dir,own)
  res , vid = retrieve_video(results,b2,g2,r2)
  print(res)
  print(vid)




