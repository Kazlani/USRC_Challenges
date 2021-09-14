# Kousha Aslani, SID: 500509782, Week 5 Challenge, some code taken from Lesson 2 / challenge 2
import cv2
import numpy as np

# Read image and use canny edge detector
frame = cv2.imread ('Week_5/Photos/collage.png')
edges = cv2.Canny(frame,100,200)


# Load pentagon from a template
pentagon = cv2.imread('Week_5/Photos/pentagon.png')
pentagonCanny = cv2.Canny(pentagon,100,200) 
#find the contours of our heart image
pentagonContours, hierarchy = cv2.findContours(pentagonCanny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
#hierarchy denotes which contours are parents and the children of those parent contours (from lesson 2 template)

# Find is contours and create a moment set for checking
pentagonBlank = np.zeros(pentagon.shape)
cv2.polylines(pentagonBlank,pentagonContours,True,(255),1)

#moment is average of intensities, which allows us to get the center of a contour
pentagonMoments = cv2.moments(pentagonContours[1]) 
pentagonHuMoments= cv2.HuMoments(pentagonMoments)

# print values
print("pentagonHuMoments:\n",pentagonHuMoments,"\n")

# Get rid of the ones with an area smaller than tiny
contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

blankImage = np.zeros(edges.shape)

goodContours=[]
for contour in contours:
    if cv2.contourArea(contour)>100:
        contourMoments = cv2.moments(contour)
        contourHuMoments = cv2.HuMoments(contourMoments)
        #find the difference between moments
        delta = np.sum(pentagonHuMoments-contourHuMoments)
        print(delta)
        if (np.abs(delta)<0.002): #0.002 is our threshold
            print(np.abs(delta))
            goodContours.append(contour)
            cv2.polylines(blankImage,contour,True,(255),1)

# Show all images
cv2.imshow("original", frame)
cv2.imshow("pentagon", pentagonBlank)
cv2.imshow("pentagonContour", pentagonCanny)
cv2.imshow("edges", edges) 
cv2.imshow("good contours", blankImage) 

cv2.waitKey(-1)
