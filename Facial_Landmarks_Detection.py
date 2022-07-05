import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
while True:
    ret,image=cap.read()
    if ret is not True:
        break
    height,width,_=image.shape
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(rgb_image)
    height, width, _ = image.shape
    for facial_landmarks in result.multi_face_landmarks:
        for i in range(0, 468):
            pt1 = facial_landmarks.landmark[i]
            x = int(pt1.x * width)
            y = int(pt1.y * height)
            cv2.circle(image, (x, y), 2, (100, 100, 0), -1)
            cv2.imshow("Facial Landmarks",image)
    if cv2.waitKey(1) & 0xFF == 27:
                break
cap.release()
cv2.destroyAllWindows()