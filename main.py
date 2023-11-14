# import cv2 from opencv
import cv2
import time
# to start a video using webcam
video = cv2.VideoCapture(0)
 # to delay by 1 sec
time.sleep(1)
first_frame = None
while True:
    check, frame = video.read()
    # time.sleep(0.2) un-comment this line to understand delay
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # to conver the image to gray scale to have simple calculations
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)
    # cv2.imshow("My video", gray_frame_gau) # displays video in a popup with frame
    if first_frame is None:
        first_frame = gray_frame_gau
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame,None,iterations=2)
    #cv2.imshow("My video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0),3)
    cv2.imshow("video", frame)
    key = cv2.waitKey(1) # creating a keyboard input instance
    if key == ord("q"): # checking if key entered is q  to exit the program
        break

video.release() # release the video resource
