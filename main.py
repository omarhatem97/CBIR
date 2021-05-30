from FeatureExtractor import *
from Evaluation import *
import os

image_path = r'./multi_images'  # database images path
query = r'./multi_images/iris1.jpg'  # input query from UI

image2 = cv2.imread(query)
b = FeatureExtractor(image2)
d = b.ColorHistogram()  # save features in database

res = []

# loop on images for the 1st time to be saved in database
for imagefile in os.listdir(image_path):
    # print(imagefile)
    image = cv2.imread(image_path + str('/') + imagefile)  # read image
    a = FeatureExtractor(image)
    c = a.ColorHistogram()  # save features in database
    # print(c)
    e = Evaluation()
    distance = e.NormalizedDifference(d, c, image)

    epsilon = 1e-4
    if(distance >= epsilon):
        res.append(imagefile)
    # print(distance)
    # res.append(distance)


print("______")

print(res)
