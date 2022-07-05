import numpy as np
import cv2 as cv
cap=cv.VideoCapture('Test.mp4')
ret,frame=cap.read()
x,y,width,height=580,30,80,150
track=(x,y,width,height)
roi=frame[y:y+height,x:x+width]
hsv_roi=cv.cvtColor(roi,cv.COLOR_BGR2HSV)
mask=cv.inRange(hsv_roi,np.array((0.,60.,32.)),
                np.array((180.,255.,255.)))
roi_hist=cv.calcHist([hsv_roi],[0],mask,[180],[0,180])
cv.normalize(roi_hist,roi_hist,0,255,cv.NORM_MINMAX)
termination=(cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT,10,1)
cv.imshow('ROI',roi)
while True:
    ret,frame=cap.read()
    if ret==True:
        hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
        dst=cv.calcBackProject([hsv],[0],roi_hist,[0,180],1)
        ret,track=cv.CamShift(dst,track,termination)
        #x,y,w,h=track
        #final=cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        #cv.imshow("Original",frame)
        pts=cv.boxPoints(ret)
        pts=np.int64(pts)
        final=cv.polylines(frame,[pts],True,(255,0,0),2)
        frame=cv.resize(final,(1200,700))
        cv.imshow('Final_Image',frame)
        k=cv.waitKey(30) & 0xff
        if k==27:
            break
    else:
        break
cv.destroyAllWindows()