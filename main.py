# import cv2 from opencv
import cv2
import time
from send_email import send_email
# to start a video using webcam
video = cv2.VideoCapture(0) # cv2.VideoCapture(0) starts the main cam of the system
 # to delay by 1 sec
time.sleep(1)
first_frame = None
status_list = []
while True:
    status = 0
    check, frame = video.read() # to read the video we started using cv2.videocapture()
    # time.sleep(0.2) un-comment this line to understand delay
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # to conver the image to gray scale to have simple calculations
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0) # we blur the image so that we can have low noise
    # cv2.imshow("My video", gray_frame_gau) # displays video in a popup with frame
    if first_frame is None: # Assign first frame to the frame of reference we wanna check the moving object
        first_frame = gray_frame_gau
    delta_frame = cv2.absdiff(first_frame, gray_frame_gau) # delta frame is abs diff betw the frames to get only whites
    """cv2.threshlod(frame, x,y, algo)[1] this method replaces x values with y with the seletcted algo and select the 
    frame with [1]"""
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2) # The dilate() function returns an image with increased size
    # of white shade in the given image.
    # cv2.imshow("My video", dil_frame)
    # findContours detects change in the image color and marks it as contour.
    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # if area of object detected is less than 5000 may be it is just some noise or not purely a object
        if cv2.contourArea(contour) < 5000:
            continue
            # cv2.boundingReact gives us coordinates of the contours
        x, y, w, h = cv2.boundingRect(contour)
        # cv2.rectangle forms a rectangle in frame with (x,y) as one end and x+w,y+h another and color
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
    status_list.append(status)
    status_list = status_list[-2:]
    if status_list[0] == 1 and status_list[1] == 1:
        # is_converted, object_image = cv2.imencode('.jpg', frame)
        cv2.imwrite('output_image.png', frame)
        send_email('output_image.png')
    cv2.imshow("video", frame)
    key = cv2.waitKey(1) # creating a keyboard input instance
    if key == ord("q"): # checking if key entered is q  to exit the program
        break

video.release() # release the video resource
