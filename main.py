import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8) # Matix of 0's 512 x 512 3 color channels 0-255

img[:] = 255, 0, 0 # Changes color in matix using BGR format

cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 5) # Draws a green line from the top left corner to the bottom right corner with thickness 5

cv2.rectangle(img, (0,0), (250, 350), (0, 0, 255), 3) # Draws a red rectangle from the top left corner to the point (250, 350) with thickness 3

cv2.rectangle(img, (350, 350), (450, 450), (255, 255, 0), cv2.FILLED) # Draws a filled cyan rectangle from the point (350, 350) to the point (450, 450)

cv2.circle(img, (400, 50), 30, (255, 0, 255), 5) # Draws a magenta circle with center at (400, 50) and radius 30 with thickness 5

cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2) # Puts the text 'OpenCV' at the point (10, 500) with font size 1 and color yellow with thickness 2

cv2.imshow('', img)

cv2.waitKey(0)
cv2.destroyAllWindows() 