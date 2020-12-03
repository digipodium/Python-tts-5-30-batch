import cv2 as cv

cap = cv.VideoCapture(0) # 0 means 1st camera, 1 means 2nd cam

while True:
    ret, frame =cap.read()
    if not ret:
        print('camera not working')
        break
    
    cv.imshow('thats me',frame)
    if cv.waitKey(1) == 27:
        break
cap.release()
cv.destroyAllWindows()
