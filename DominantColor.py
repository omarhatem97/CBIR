import numpy as np
import cv2
from matplotlib import colors, pyplot as plt



def unique_count_app(img):
    a=cv2.imread(img)
    a=cv2.resize(a,(512,512))
    colors, count = np.unique(a.reshape(-1,a.shape[-1]), axis=0, return_counts=True)
    #print(colors[count.argmax()])

    return colors[count.argmax()]

### for debugging###
img1=cv2.imread('orange3.jpg')
img2=cv2.imread('orange1.jpg')
x=unique_count_app('orange3.jpg')
#y=unique_count_app(img2)
print(x)
#print(y)
