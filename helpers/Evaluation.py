import cv2
import numpy as np



class Evaluation:
    
    def __init__(self):
        
        self.distance=0
        
        
    def NormalizedDifference(self, hist_queryimage , hist_database_image , database_image):
        
        height,width = database_image.shape[:2]
        num_of_pixels = width*height
        self.summation_intersection = 0       
        for (q, d) in zip(hist_queryimage, hist_database_image):
            self.summation_intersection += min(q, d)
  
        
        self.distance = self.summation_intersection / num_of_pixels
        
        return self.distance
        

        
        
        
        