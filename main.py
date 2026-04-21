import cv2


#vid = cv2.VideoCapture('video.mp4')
vid = cv2.VideoCapture(1) # Opens the second camera (webcam) for video capture

vid.set(3, 640) # Sets the width of the video frame to 640 pixels
vid.set(4, 480) # Sets the height of the video frame to 480

# Loop for playing the video
while True:
    success, img = vid.read() # Reads a frame from the video and stores it in img, while storing success as a boolean indicating if the read was successful
    cv2.imshow("Video", img)
 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cv2.destroyAllWindows() # Clean up and close all OpenCV windows