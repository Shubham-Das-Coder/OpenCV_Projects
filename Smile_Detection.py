import cv2

cascade_face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cascade_smile=cv2.CascadeClassifier('haarcascade_smile.xml')

cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()
    g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    f=cascade_face.detectMultiScale(g,scaleFactor=1.3,minNeighbors=5,minSize=(30,30))
    
    for(x,y,w,h) in f:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        gray_r=g[y:y+h,x:x+w]
        
        s=cascade_smile.detectMultiScale(gray_r,scaleFactor=1.5,minNeighbors=15,minSize=(25,25))
        
        for i in s:
            if len(s)>1:
                cv2.putText(img,"SMILING",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2,cv2.LINE_AA)
    
    cv2.imshow('Video',img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()