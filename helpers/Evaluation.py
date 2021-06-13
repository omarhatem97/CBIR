import cv2
import numpy as np
import pickle
from Videohistogram import *


class Evaluation:
    
    def __init__(self):
        
        self.distance=0
        
        
    def colorLayoutDifference(self, hist_queryimage , hist_database_image ):
        
        
        num_of_pixels = 512*512
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
        

    def meanColorDifference(self, img1,img2):

        diff=np.abs(img1-img2)
        error=np.sum(diff)
        return error


    
    def retrieve_video(self,results,b2,g2,r2, query_video):
        """
        get the names and values of errors for the best match five videos in the database under threshold.
        :param results: list of histograms and files names of videos in database
        :param b2: database video green
        :param g2: database video red
        :param r2: query video blue
        :return: best match video name, list of the best five match videos under threshold
        """
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
            histogram_generator1 = Histogram(dir, query_video)
            avg = histogram_generator1.match(b2,g2,r2,arr,arr2,arr3)
            table_data.append([arr4, round(avg, 5)])
            if i == 0:
                video_match = arr4
                video_match_value = avg
            else:
                if avg < video_match_value:
                    video_match = arr4
                    video_match_value = avg
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
                res.append(sorted_res[0])
        
        return res, video_match
        
        
        