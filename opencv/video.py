import cv2 as cv

capture = cv.VideoCapture('hzd.mkv')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame) #fragment

    if cv.waitKey(20) & 0xFF == ord('q'): #q close video
        break

capture.release()
cv.destroyAllWindows()
