import cv2

#reading images from main folder
img = cv2.imread('Hackerman.jpg')
cv2.imshow('Meme', img)

cv2.waitKey(0)
