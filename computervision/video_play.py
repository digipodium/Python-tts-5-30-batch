import cv2 as cv
import numpy as np
from numpy.lib.function_base import flip
cap = cv.VideoCapture('C:/Users/xaidi/Videos/Captures/example.mp4') # 0 means 1st camera, 1 means 2nd cam

while True:
    ret, frame =cap.read()
    if not ret:
        print('video not playing')
        break
    print(frame.shape)
    smframe = cv.resize(frame,(1920//2,1080//2)) # half of original
    grframe = cv.cvtColor(smframe,cv.COLOR_BGR2RGB)
    flipframe= cv.flip(smframe,2)
    flipframe2= cv.flip(smframe,-4)
    cv.imshow('thats me',smframe)
    cv.imshow('thats not me',grframe)
    cv.imshow('thats not me flipped',flipframe)
    
    mirrorframe = np.hstack((smframe,flipframe))
    mirrorframe2 = np.vstack((smframe,flipframe2))
    cv.imshow('amazing',mirrorframe)
    cv.imshow('amazing2',mirrorframe2)
    if cv.waitKey(1) == 27:
        break
cap.release()
cv.destroyAllWindows()
