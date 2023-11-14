# import cv2 from opencv
import cv2
import time
# to start a video using webcam
video = cv2.VideoCapture(0)
 # to delay by 1 sec
time.sleep(1)
# check, frame = video.read()
# cv2.imwrite("test1.png", frame)
# print(check)
# print(frame)
while True:
    check, frame = video.read()
    # time.sleep(0.2) un-comment this line to understand delay
    cv2.imshow("My video", frame) # displays video in a popup with frame
    key = cv2.waitKey(1) # creating a keyboard input instance
    if key == ord("q"): # checking if key entered is q  to exit the program
        break

video.release() # release the video resource
