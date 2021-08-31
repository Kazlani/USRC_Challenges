import cv2

original = cv2.imread('Hackerman.jpg')
cv2.imshow('HackermanOriginal',original)

# Find dimensions of image, then half to find original center

# Function taken from 2_resizeRescale.py)
def rescale_frame(frame,scale=1):
    #works for images, video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions = (width,height)

    return cv2.resize(frame,dimensions,interpolation =cv2.INTER_AREA)

# Rescaled
rescaled = rescale_frame(original,0.5)
cv2.imshow('RescaledHackerman', rescaled)

# Find dimensions of original image, then half to find centre
new_width = int(original.shape[1]/2)
new_height = int(original.shape[0]/2)

# Circle layer
circleImage = cv2.circle(original,(new_width,new_height),20,(255,0,0),thickness=2)
cv2.imshow('CircleHackerman',circleImage)

# Greyscale layer
greyscale=cv2.cvtColor(original,cv2.COLOR_BGR2GRAY)
cv2.imshow('GreyscaleHackerman',greyscale)

# Blurred layer
blurred=cv2.GaussianBlur(original,(9,9),cv2.BORDER_DEFAULT)
cv2.imshow('BlurredHackerman',blurred)

# Canny layer
canny=cv2.Canny(original,125,200)
cv2.imshow('Canny',canny)

# Rotation layer (function taken from 5_imageTransformation.py)
def rotate(img, angle, rotPoint=None):
    (height,width)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(width//2,height//2)
    
    rotMat = cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
    dimensions =(width,height)

    return cv2.warpAffine(img,rotMat,dimensions)

rotated= rotate(original,45)
cv2.imshow('RotatedHackerman',rotated)

cv2.waitKey(0)
