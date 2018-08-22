import cv2
import numpy
cap = cv2.VideoCapture(0)
while True :
	ret,img=cap.read()
	cv2.imshow('video output',img)
	k = cv2.waitKey(1)
	if k==ord('s'):
		break
cap.release()
cv2.destroyAllwindown()