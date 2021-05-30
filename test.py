from FeatureExtractor import *
import cv2 as cv
from helpers.Evaluation import *
import os

image_path = r'./multi_images'  # database images path
query = r'./multi_images/orange1.jpg'  # input query from UI

image2 = cv.imread(query)
b = FeatureExtractor(image2)
d,epsilon = b.ColorLayout()  # save features in database

res = []

# loop on images for the 1st time to be saved in database
for imagefile in os.listdir(image_path):
    # print(imagefile)
    image = cv.imread(image_path + str('/') + imagefile)  # read image
    a = FeatureExtractor(image)
    c, epsilon = a.ColorLayout()  # save features in database
    # print(c)
    e = Evaluation()
    distance = e.colorLayoutDifference(d, c, image)
    print(distance)
    if(distance >= epsilon):
        res.append(imagefile)
    # print(distance)
    # res.append(distance)


print("______")

print(res)
