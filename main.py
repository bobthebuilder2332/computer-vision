import cv2
import numpy as np

img = cv2.imread('image2.jpg')

w, h = 250, 350

points1 = np.float32([[111, 219], [287, 188], [154, 482], [352, 440]]) # Points of the image to be transformed
points2 = np.float32([[0, 0], [w, 0], [0, h], [w, h]]) # Points of the output image (the rectangle to which the original points will be mapped)

matrix = cv2.getPerspectiveTransform(points1, points2) # Calculate the perspective transformation matrix based on the corresponding points

imgOut = cv2.warpPerspective(img, matrix, (w, h)) # Apply the perspective transformation to the original image using the calculated matrix and specify the size of the output image (w, h)

cv2.imshow('Image', img)
cv2.imshow('ImageOut', imgOut)

cv2.waitKey(0)
cv2.destroyAllWindows()