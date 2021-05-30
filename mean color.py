import cv2
import numpy as np
from matplotlib import colors, pyplot as plt

threshold=155



def mean_color(img):
    image_bgr=cv2.imread(img,cv2.IMREAD_COLOR)
    #cv2.imshow('cv',image_bgr)
    #cv2.waitKey(0) 
    #cv2.destroyAllWindows() 
    
    colors=cv2.mean(image_bgr)
   
    observation=np.array([(colors[2],colors[1],colors[0])])
    #print(observation)
    # plt.imshow(observation)
    # plt.show()
    return observation



def compare(img1,img2):
    x=mean_color(img1)
    y=mean_color(img2)
    diff=np.abs(x-y)
    error=np.sum(diff)
    if error<threshold:
        
        print(error)
    else:
        print('NOO')


    



if __name__ == "__main__":
 # x= mean_color('orange.jpg')
  
 # y=mean_color('orange2.jpg')
 compare('apple.jpg','apple1.jpg')