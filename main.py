import cv2
import numpy as np


img = cv2.imread('image.jpg')
imgResize = cv2.resize(img, (300, 200))
imgCrop = img[0:200, 200:500] # Crops image [y1:y2, x1:x2]

print(img.shape) # Prints shape of image (height, width, channels[colors])
print(imgResize.shape)
print(imgCrop.shape)

cv2.imshow('image', img)
cv2.imshow('image resize', imgResize)
cv2.imshow('image crop', imgCrop)

cv2.waitKey(0)
cv2.destroyAllWindows()