import cv2


vid = cv2.VideoCapture('video.mp4')

# Loop for playing the video
while True:
    success, img = vid.read() # Reads a frame from the video and stores it in img, while storing success as a boolean indicating if the read was successful
    cv2.imshow("Video", img)

    """
    Breaks out of loop and closes program if the 'q' key is pressed

    waitKey(1) waits for 1 millisecond while returning the ASCII code of any key pressed
    & is a bitwise AND operator that returns 1 if both are 1 and 0 otherwise
    0xFF is the hexadecimal literal for 255, used for masking
        Together they "cut" everything out of the 32 bit return value, leaving only the last 8 bits which represent the ASCII code of the key pressed
    ord('q') returns the Unicode value for the character 'q'
    """
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cv2.destroyAllWindows() # Clean up and close all OpenCV windows