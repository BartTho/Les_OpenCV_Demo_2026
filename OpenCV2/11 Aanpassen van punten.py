import cv2
import numpy as np

img = cv2.imread('opencv.jpg')

px = img[100,100]
print(px)

# accessing only blue pixel
blauw = img[100,100,0]
print (blauw)
img[100,100] = [255,255,255]
print(img[100,100])

# accessing RED value
img.item(10,10,2)

# modifying RED value
img[10, 10, 2] = 100
img.item(10,10,2)

print(img.shape)
print(img.size)
print(img.dtype)