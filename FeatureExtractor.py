import cv2
import numpy as np

class FeatureExtractor:
    
    def __init__(self,image):
        self.image=image
        
 
    def ColorHistogram(self):
        
        image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV )
        image = cv2.resize(image,(512,512))
        features = 0
        hist = cv2.calcHist([image], [0,1,2],None,[10,10,4],[0, 180, 0, 256,0,256])  
        features = cv2.normalize(hist,features)

        return features
                
                
                




    
   
        
