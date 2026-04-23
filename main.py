import cv2
import numpy as np

img = cv2.imread('image.jpg')


# Stacking has to be done on images with thes same channels (i.e. RGB doesn't work with BGR or grayscale)
hor = np.hstack((img, img)) # Stacks matrices horizontally (column-wise)
ver = np.vstack((img, img)) # Stacks matrices vertically (row-wise)

cv2.imshow('Image', hor)
cv2.imshow('Image2', ver)

cv2.waitKey(0)
cv2.destroyAllWindows()