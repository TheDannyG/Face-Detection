#Detects faces realtime using OpenCV and uses AWS Rekognition to identify people agianst face collection stored in AWS
# needs search_faces.py
#============================================================================================

import cv2
import sys
import logging as log
import datetime as dt

from time import sleep
import boto3
from search_faces import search_face 

#Create classifier
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0
frame_cnt = 0
faces = []
face_name = ''

#connect to AWS
client = boto3.client('rekognition')

#set collection name
collection_name = 'authorized_faces'
match_threshold = 0.9


while True:
	if not video_capture.isOpened():
		print('Unable to load camera.')
		sleep(5)
		pass

	# Capture frame-by-frame
	ret, frame = video_capture.read()
	
	frame_cnt = frame_cnt + 1
	
	# Check for faces every 10 frames
	if frame_cnt == 10:
		frame_cnt = 0

		#convert into grey
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		#detect faces
		faces = faceCascade.detectMultiScale(
			gray,
			scaleFactor=1.1,
			minNeighbors=5,
			minSize=(30, 30)
		)


	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		# Write face name
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame,face_name,(x,y), font, 1,(0,255,0),2)

	# write log
	if anterior != len(faces):
		anterior = len(faces)
		log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))

	#Read keys
	key = cv2.waitKey(1) & 0xFF    

	#Quit on 'q'
	if key == ord('q'):
		break
	
	#Detect face on 'd'
	if key == ord('d'):
		face_name = search_face(client, cv2.imencode('.jpg', frame)[1].tostring(), collection_name, match_threshold)
		print (face_name)
	
	# Display the resulting frame
	cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
