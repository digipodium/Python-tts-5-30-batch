import cv2 as cv # we are using opencv 4
import numpy as np

frame = cv.imread('contactcard.png')
print(frame.shape)
print(frame.ndim)
print(frame.size)
smframe = cv.resize(frame,(1920//4,1080//4))
grayimg = cv.cvtColor(smframe,cv.COLOR_BGR2GRAY)
hsvimg = cv.cvtColor(smframe,cv.COLOR_BGR2HSV)
rgbimg = cv.cvtColor(smframe,cv.COLOR_BGR2RGB)
mathimg = smframe * 10

# cv.imshow('image window',smframe)
cv.imshow('gray window',grayimg)
imgstack = np.hstack((smframe,hsvimg,rgbimg,mathimg))
cv.imshow("all img",imgstack)

cv.waitKey(0)
