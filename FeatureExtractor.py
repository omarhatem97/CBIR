import cv2
import numpy as np

class FeatureExtractor:
    
    def __init__(self,image):
        self.image=image
        
 
    def ColorHistogram(self):
        
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV )
        image = cv2.resize(image,(512,512))
        features = []
        
        (h, w) = image.shape[:2]
        x,y= (int(w*0.5) , int(h*0.5)) #center
        
              
        
        for row in range(0,w , x):
            for coloumn in range(0,h , y):
                
                window = image[row:row+x,coloumn:coloumn+y]  
                
                #hardcoded bins
                hist = cv2.calcHist([window], [0,1,2],None,[10,10,4],[0, 180, 0, 256,0,256])  
                hist =  cv2.normalize(hist,hist).flatten()
                features.extend(hist)
        return features
                
                
                




    
   
        
