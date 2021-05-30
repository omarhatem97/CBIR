import cv2 as cv
import numpy as np
from matplotlib import colors, pyplot as plt


class FeatureExtractor:
    
    def __init__(self,image):
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
        epsilon = 1e-4
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
        return features, epsilon

    
    def mean_color(img):

        image_bgr=cv.imread(img,cv.IMREAD_COLOR)
        #cv.imshow('cv',image_bgr)
        #cv.waitKey(0) 
        #cv.destroyAllWindows() 
        
        colors=cv.mean(image_bgr)
    
        observation=np.array([(colors[2],colors[1],colors[0])])
        print(observation)
        plt.imshow(observation)
        plt.show()
        return observation
                
                




    
   
        
