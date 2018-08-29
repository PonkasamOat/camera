import cv2
import numpy

#ตรวจจับหน้า
def face():
	print ("Write Code Here ....")
	#write code

#เปิดการทำงานกล้อง
print("Open Camera")
cap = cv2.VideoCapture(0)

#ลูบ วนการทำงาน 
while True :
	print ("Start Loop 2")
	ret,img=cap.read()
	cv2.imshow('video output',img)
	
	#call function ตรวจจับหน้า
	face()
	
	k = cv2.waitKey(1)
	#ะสั่งหยุดต่อเมื่อ กดตัว S 
	if k==ord('s'):
		break
#ปิดกล้อง
cap.release()
#ปิดหน้าต่าง
cv2.destroyAllwindown()



 