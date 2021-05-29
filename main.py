from FeatureExtractor import *
from Evaluation import *
import  os


image_path = r'./multi_images' #database images path
query = r'./multi_images/orange1.jpg' #input query from UI




for imagefile in os.listdir(image_path): #loop on images for the 1st time to be saved in database
    
    image =  cv2.imread(image_path+str('/')+imagefile)     
    a = FeatureExtractor(image)  
    c = a.ColorHistogram()   # save features in database

