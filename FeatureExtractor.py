import cv2 as cv
import numpy as np
from matplotlib import colors, pyplot as plt
from Videohistogram import *
from db import *
import pickle


class FeatureExtractor:
    
    def __init__(self,image=None):
        self.image=image
    

    def Histogram(self):
        #Histogram algorithm   
        image = cv.cvtColor(self.image, cv.COLOR_BGR2HSV )
        image = cv.resize(image,(512,512))
        features = 0
        hist = cv.calcHist([image], [0,1,2],None,[10,10,4],[0, 180, 0, 256,0,256])  
        features = cv.normalize(hist,features)

        return features

    

    
    def ColorLayout(self):
        #color layout algorithm
        epsilon = 1e-5
        image = cv.cvtColor(self.image, cv.COLOR_BGR2HSV )
        image = cv.resize(image,(512,512))
        features = []
        
        (h, w) = image.shape[:2]
        x,y= (int(w*0.5) , int(h*0.5)) #center
        
              
        
        for row in range(0 ,w , x):
            for coloumn in range(0,h , y):
                
                window = image[row:row+x,coloumn:coloumn+y]  
                
                #hardcoded bins
                hist = cv.calcHist([window], [0,1,2],None,[10,10,4],[0, 180, 0, 256,0,256])  
                hist =  cv.normalize(hist,hist).flatten()
                features.extend(hist)
        return features

    
    def mean_color(self):
        
        epsilon = 100
        image_bgr=self.image  
        image_bgr=cv.resize(image_bgr,(512,512))
        colors=cv.mean(image_bgr)    
        observation=np.array([(colors[2],colors[1],colors[0])])
        # print(observation)
        # plt.imshow(observation)
        # plt.show()
        return observation


    def Dominant_color(self):
       epsilon = 700
       a=self.image
       a=cv.resize(a,(512,512))
       colors, count = np.unique(a.reshape(-1,a.shape[-1]), axis=0, return_counts=True)
       #print(colors[count.argmax()])
    
       return colors[count.argmax()]     
                
    def test_video(self,dir, query_video):
        """
        get the value of red,green,blue colors histogram for a test video, and select all green , color , red
        of another videos from the database.
        :param dir: directory of the test video
        :param own: the name of the video mp4 format in the directory 
        :return: list of selected histograms from the database and the name of the videos, red , blue , green colors for the test video
        """
        database = DB("cbDatabase")

        mycursor = database.get_cursor()
        histogram_generator = Histogram(dir, query_video)
        b2,g2,r2 = histogram_generator.generate_and_store_average_rgb_histogram()
        mycursor.execute("SELECT B , G , R , Name , Path FROM VideosDB")
        results = mycursor.fetchall()
        return results,b2,g2,r2



    
   
        
