import cv2
import numpy as np



class Evaluation:
    
    def __init__(self):
        
        self.distance=0
        
        
    def NormalizedDifference(self, hist_queryimage , hist_database_image , database_image):
        
        height,width = database_image.shape[:2]
        num_of_pixels = width*height
 
        intersection=0
        intersection = cv2.compareHist(hist_queryimage, hist_database_image, cv2.HISTCMP_INTERSECT)
        
        self.distance =  intersection / num_of_pixels
        
        return self.distance
        

        
        
        
        