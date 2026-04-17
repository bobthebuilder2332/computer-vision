import cv2

img = cv2.imread('image.png') # Import the image file "image.png"
cv2.imshow('Image', img) # Display the image in a window titled "Image"
cv2.waitKey(0) # Wait until user presses key "0" to close the window
cv2.destroyAllWindows() # Close all OpenCV windows