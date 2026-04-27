import cv2
import numpy as np


def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # cv2.RETR_EXTERNAL = only external contours, cv2.CHAIN_APPROX_NONE = all points of contour
    for contour in contours:
        area = cv2.contourArea(contour)
        print(area)
        if area > 500:
            # Make sure to visually check if every shape is included
            cv2.drawContours(imgContours, contour, -1, (255, 0, 0), 3) # -1 = all contours, (255, 0, 0) = blue color, 3 = thickness
            perimeter = cv2.arcLength(contour, True) # True = closed contour
            approx = cv2.approxPolyDP(contour, .02 * perimeter, True) # Returns the reduced amount of points on the contour: 0.02 = accuracy, True = closed contour
            objectCorners = len(approx)
            x, y, w, h = cv2.boundingRect(approx) # Create a bounding box around the contour: x and y = top left corner, w and h = width and height of the boxcv2.rectangle(imgContours, (x, y), (x + w, y + h), (0, 255, 0), 3) # Draw bounding box: (0, 255, 0) = green color, 3 = thickness

            if objectCorners == 3: objectType = 'Triangle'
            elif objectCorners == 4:
                aspectRatio = w / float(h) # Cast before to avoid rounded quotient
                if aspectRatio > 0.95 and aspectRatio < 1.05: objectType = 'Square' # Slight error room for square
                else: objectType = 'Rectangle'
            elif objectCorners > 4: objectType = 'Circle' # Only works here because there are only 3 types of shapes
            else: objectType = 'None'

            cv2.rectangle(imgContours, (x, y), (x + w, y + h), (0, 255, 0), 3) # Draw bounding box: (0, 255, 0) = green color, 3 = thickness
            cv2.putText(imgContours, objectType, (x, y + h + 30), cv2.FONT_HERSHEY_COMPLEX, .7, (0, 255, 0), 2) # Put text in the middle of the bounding box: (0, 255, 0) = green color, 2 = thickness

img = cv2.imread('image2.png')

imgBlank = np.zeros_like(img) # Blank image with same dimensions as img
imgContours = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1) # Higher 3rd value = more blur
imgCanny = cv2.Canny(imgBlur, 50, 50) # Higher 2nd and 3rd value = more edges detected

getContours(imgCanny)
imgStack = stackImages(0.6, ([img, imgGray, imgBlur], [imgCanny, imgContours, imgBlank]))
cv2.imshow('Stacked Images', imgStack)

cv2.waitKey(0)
cv2.destroyAllWindows()