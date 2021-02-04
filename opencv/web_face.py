import cv2

face_case = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    # img = cv2.imread("putin.jpeg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Gray', gray)

    faces = face_case.detectMultiScale(img, 1.1, 19)

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (12, 22, 0), 5)
    cv2.imshow('rez', img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()
