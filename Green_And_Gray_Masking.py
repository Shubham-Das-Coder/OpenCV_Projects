import cv2
import numpy as np
cap=cv2.VideoCapture(0)
object_detector=cv2.createBackgroundSubtractorMOG2()
while True:
    ret,frame=cap.read()
    mask=object_detector.apply(frame)
    cv2.imshow("Frame",frame)
    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cv2.drawContours(frame,[cnt],-1,(0,255,0),2)
    cv2.imshow("Mask",mask)
    cv2.imshow("Frame",frame)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()