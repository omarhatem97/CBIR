import cv2
import numpy as np
from matplotlib import colors, pyplot as plt
threshold=100
def mean_color(img):
    image_bgr=cv2.imread(img,cv2.IMREAD_COLOR)
   

    
    colors=cv2.mean(image_bgr)
    print(colors)
   
    observation=np.array([(colors[2],colors[1],colors[0])])
    print(observation)
    #plt.imshow(observation)
    #plt.show()


    return observation



def compare(img1,img2):
    x=mean_color(img1)
   
 
    y=mean_color(img2)

    diff=np.abs(x-y)
    error=np.sum(diff)
    print(error)
    if error<threshold:
        
        print('Yes')
    else:
        print('NOO')


    



if __name__ == "__main__":
 

 
 compare('sea.jpeg','orange3.jpg')