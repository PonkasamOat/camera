import cv2
import numpy

#ตรวจจับหน้า
def face():
	print "Write Code Here ...."
	#write code

#เปิดการทำงานกล้อง
cap = cv2.VideoCapture(0)

#กดตุ่มเพื่อเริ่มการทำงาน O
while True :
	k = cv2.waitKey(1)
	if k==ord('o'):	
		break;
		
#ลูบ วนการทำงาน 
while True :
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



 