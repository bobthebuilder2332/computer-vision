import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Internal path for loading the Haar Cascade XML file
img = cv2.imread('image3.png')

imgGray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4) # Detect faces of different sizes in the image, 1.1 is the scale factor and 4 is the minimum number of neighbors

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x + w, y + h), (255, 0, 0), 2) # Draw a rectangle around the detected faces

cv2.imshow('Image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()