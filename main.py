import cv2


img = cv2.imread('image.png')

cv2.imshow("Image", img) # Creates window with img but doesn't render until waitKey()

cv2.waitKey(0) # Wait indefinitely until a key is pressed

cv2.destroyAllWindows() # Close all OpenCV windows