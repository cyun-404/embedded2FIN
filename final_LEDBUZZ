import cv2
import sys
import RPi.GPIO as GPIO
import time


cap = cv2.VideoCapture(0)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.OUT)
GPIO.output(16,GPIO.LOW)
#p=GPIO.PWM(16,100)
#p.start(0)
# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# Our operations on the frame come here
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# Detect faces in the image
	faces = faceCascade.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30)
		#flags = cv2.CV_HAAR_SCALE_IMAGE
	)

	print("Found {0} faces!".format(len(faces)))
		
	#else GPIO.output(signalPIN, GPIO.LOW)
    
	# Draw a rectangle around the faces
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
		
	# Display the resulting frame
	cv2.imshow('frame', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
GPIO.cleanup()
cv2.destroyAllWindows()
