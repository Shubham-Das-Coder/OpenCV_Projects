import cv2
import numpy as np
cap=cv2.VideoCapture(0)
object_detector=cv2.createBackgroundSubtractorMOG2()
while True:
    ret,frame=cap.read()
    mask=object_detector.apply(frame)
    cv2.imshow("Frame",frame)
    cv2.imshow("Mask",mask)
    if cv2.waitKey(1)==27:
        break
cap.release()
cv2.destroyAllWindows()