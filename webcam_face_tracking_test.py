import cv2
import sys
#code to test index_face function (from index_faces.py)
import os
os.chdir('/home/dad/AWS/Face-Detection')
 
if __name__ == '__main__' :
 
	# Set up tracker.
	# Instead of MIL, you can also use
	# BOOSTING, KCF, TLD, MEDIANFLOW or GOTURN
	# Define an initial bounding box
	bbox = (0, 0, 0, 0)
	frame_cnt = 0
	
	tracker = cv2.Tracker_create("KCF")

	#Create classifier
	faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
 
	# Read video
	video = cv2.VideoCapture(0)
 
	# Exit if video not opened.
	if not video.isOpened():
		print ("Could not open video")
		sys.exit()
 
	# Read first frame.
	ok, frame = video.read()
	if not ok:
		print ('Cannot read video file')
		sys.exit()
		
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
		bbox = (x, y, w, h)
		

	# Initialize tracker with first frame and bounding box
	ok = tracker.init(frame, bbox)
 
	while True:
		frame_cnt = frame_cnt + 1
		# Read a new frame
		ok, frame = video.read()
		if not ok:
			break

		if frame_cnt == 100:
			frame_cnt = 0
			print ("100")
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
				bbox = (x, y, w, h)
				print (bbox)
				
			# Initialize tracker with first frame and bounding box
			tracker = cv2.Tracker_create("KCF")
			ok = tracker.init(frame, bbox)
			# Update tracker
			ok, bbox = tracker.update(frame)
		
		# Update tracker
		ok, bbox = tracker.update(frame)
 
		# Draw bounding box
		if ok:
			p1 = (int(bbox[0]), int(bbox[1]))
			p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
			cv2.rectangle(frame, p1, p2, (0,0,255))
 
		# Display result
		frame = cv2.flip(frame, 1)
		cv2.imshow("Tracking", frame)
 
		# Exit if ESC pressed
		k = cv2.waitKey(1) & 0xff
		if k == 27 : break