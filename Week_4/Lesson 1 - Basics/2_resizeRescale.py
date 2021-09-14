#Resizing and Rescaling

import cv2

#img = cv2.imread('Photos\cat_large.jpg')
#cv2.imshow('Cat',img)

def rescale_frame(frame,scale=0.75):
    #works for images, video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation =cv2.INTER_AREA)

#cv2.waitKey(0)

### FUNCTION POINTLESS ON MAC AS WEBCAM HAS FIXED RESOLUTION ### 
# def change_res(width,height):
#     #only works for live video
#     capture.set(3,width) #3 for width
#     capture.set(4,height) #4 for height

#reading videos

# capture = cv2.VideoCapture('../Videos/kitten.mp4')
# VideoCapture(0) = Webcam input
capture=cv2.VideoCapture(0)
# change_res(160,120)

while True:
    isTrue, frame=capture.read()

    # cv2.imshow("video with set", frame)
    # cv2.imshow("Video Resized", frame_resized)
    
    #recsale video frame
    frame_resized = rescale_frame(frame, scale = 0.5)

    cv2.imshow('video with set',frame)
    cv2.imshow('Resized',frame_resized)

    #20 is the delay
    if cv2.waitKey(20) & 0xFF==ord('d'):
        break




capture.release()
cv2.destroyAllWindows()