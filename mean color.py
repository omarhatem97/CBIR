import cv2
import numpy as np
from matplotlib import colors, pyplot as plt

def mean_color(img):
    image_bgr=cv2.imread(img,cv2.IMREAD_COLOR)
    #cv2.imshow('cv',image_bgr)
    #cv2.waitKey(0) 
    #cv2.destroyAllWindows() 
    
    colors=cv2.mean(image_bgr)
   
    observation=np.array([(colors[2],colors[1],colors[0])])
    print(observation)
    plt.imshow(observation)
    plt.show()
    return observation





if __name__ == "__main__":
  x= mean_color('orange.jpg')
  
  y=mean_color('orange2.jpg')
  print(x)
  print(y)




