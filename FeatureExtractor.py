import cv2 as cv
import numpy as np

class FeatureExtractor:
    
    def __init__(self,image):
        self.image=image
        
 
    def ColorHistogram(self):
        
        image = cv.cvtColor(self.image, cv.COLOR_BGR2HSV )
        image = cv.resize(image,(512,512))
        features = []
        
        (h, w) = image.shape[:2]
        x,y= (int(w*0.25) , int(h*0.25)) #center
        
              
        
        for row in range(0 ,w , x):
            for coloumn in range(0,h , y):
                
                window = image[row:row+x,coloumn:coloumn+y]  
                
                #hardcoded bins
                hist = cv.calcHist([window], [0,1,2],None,[10,10,4],[0, 180, 0, 256,0,256])  
                hist =  cv.normalize(hist,hist).flatten()
                features.extend(hist)
        return features
                
                
                




    
   
        
