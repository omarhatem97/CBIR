from FeatureExtractor import *
from helpers.Evaluation import *
import  os


image_path = r'./multi_images' #database images path
query = r'./multi_images/31.jpg' #input query from UI

image2 =  cv2.imread(query) 
a = FeatureExtractor(image2)  
d = a.Histogram() 
res = []
c = []
for imagefile in os.listdir(image_path): #loop on images for the 1st time to be saved in database
    
    image =  cv2.imread(image_path+str('/')+imagefile)     
    a = FeatureExtractor(image)  
    c = a.Histogram()   # save features in database
    # print(c)
    e = Evaluation()
    distance = e.HistogramNormalizedDifference(d,c , image) 
    if(distance >= 4.2e-06):
        res.append(imagefile)
    print(imagefile)
    print(distance)

print(res)
# print(c)