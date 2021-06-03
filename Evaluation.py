import cv2
import numpy as np
from FeatureExtractor import *


class Evaluation:
    
    def __init__(self):
        
        self.distance=0
        
        
    def colorLayoutDifference(self, hist_queryimage , hist_database_image , database_image):
        
        height,width = database_image.shape[:2]
        num_of_pixels = width*height
        self.summation_intersection = 0       
        for (q, d) in zip(hist_queryimage, hist_database_image):
            self.summation_intersection += min(q, d)
  
        
        self.distance = self.summation_intersection / num_of_pixels
        
        return self.distance


    def HistogramNormalizedDifference(self, hist_queryimage , hist_database_image , database_image):
            
        height,width = database_image.shape[:2]
        num_of_pixels = width*height
 
        intersection=0
        intersection = cv2.compareHist(hist_queryimage, hist_database_image, cv2.HISTCMP_INTERSECT)
        
        self.distance =  intersection / num_of_pixels
        
        return self.distance
        

    
    def compare(img1,img2):
        
        x=FeatureExtractor.mean_color(img1)
        y=FeatureExtractor.mean_color(img2)
         
        diff=np.abs(x-y)
        error=np.sum(diff)
        return error
            
        
        