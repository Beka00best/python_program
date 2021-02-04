import cv2 as cv

img = cv.imread('putin.jpeg') #image read
cv.imshow('Putin', img)

cv.waitKey(0) #not stop show
