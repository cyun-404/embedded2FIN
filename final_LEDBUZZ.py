import cv2
import sys
import RPi.GPIO as GPIO
import time


cap = cv2.VideoCapture(0)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.output(16,GPIO.LOW)

# haar cascade 생성
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while(True):
	# frame으로 캡쳐
	ret, frame = cap.read()

	# RGB->Gray
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# 이미지에서 얼굴 검출
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces))) # 얼굴을 찾으면 1, 아니면 0을 출력
    
	# 얼굴에 네모박스 바운딩
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	if ((len(faces))!=0):
		GPIO.output(16,GPIO.HIGH)
		print("BUZZ,LED ON")
		time.sleep(2.0)
		#p.ChangeDutyCycle(12.5)
	else :
		GPIO.output(16,GPIO.LOW)
		print("BUZZ,LED OFF")
		#p.ChangeDutyCycle(2.5)
		
	# 결과 프레임 보여줌
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# 캡쳐 release하고 GPIO 
cap.release()
GPIO.cleanup()
cv2.destroyAllWindows()
