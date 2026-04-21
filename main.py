import cv2


img = cv2.imread('image.png')

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converts image to grayscale; remmeber opencv uses BGR format instead of RGB

imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) # Blurs the image using a Gaussian filter; the (7, 7) is the kernel size (must be odd), and 0 is the standard deviation in X and Y direction

cv2.imshow('Gray Image', imgGray)
cv2.imshow('Blurred Image', imgBlur)
cv2.waitKey(0)

cv2.destroyAllWindows()