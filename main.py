import cv2
import numpy as np


img = cv2.imread('image.jpg')

kernel = np.ones((7,7), np.uint8) # Creates a kernel for dilation; the (5, 5) is the size of the kernel, and np.uint8 is the data type of the kernel elements

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converts image to grayscale; remmeber opencv uses BGR format instead of RGB
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) # Blurs the image using a Gaussian filter; the (7, 7) is the kernel size (must be odd), and 0 is the standard deviation in X and Y direction
imgCanny = cv2.Canny(imgBlur, 100, 100) # Detects edges in the image using the Canny edge detection algorithm; the two 100s are the lower and upper thresholds for the hysteresis procedure
imgDilated = cv2.dilate(imgCanny, kernel, iterations=1) # Dilates the edges in the image; the (7, 7) is the kernel size for dilation, and iterations=1 means it will be applied once
imgEroded = cv2.erode(imgDilated, kernel, iterations=1) # Erodes the dilated image; the (7, 7) is the kernel size for erosion, and iterations=1 means it will be applied once

cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blurred Image', imgBlur)
cv2.imshow('Canny Image', imgCanny)
cv2.imshow('Dilated Image', imgDilated)
cv2.imshow('Eroded Image', imgEroded)
cv2.waitKey(0)

cv2.destroyAllWindows()