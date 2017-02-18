# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 20:49:56 2017

@author: Daniel
"""

import boto3
import cv2
from datetime import datetime

startTime = datetime.now()

camera_port = 0 
ramp_frames = 5
camera = cv2.VideoCapture(camera_port)
def get_image():
 retval, im = camera.read()
 return im 
for i in xrange(ramp_frames):
 temp = camera.read()

camera_capture = get_image()
filename = "target.jpg"
cv2.imwrite(filename,camera_capture)
del(camera)

SIMILARITY_THRESHOLD = 0

if __name__ == '__main__':   
    client = boto3.client(
        'rekognition',
        region_name = 'us-east-1', 
        aws_access_key_id = 'accesskey',
        aws_secret_access_key = 'secretaccesskey',
)

    # Our source image: http://i.imgur.com/OK8aDRq.jpg
    with open('Daniel.jpg', 'rb') as source_image:
        source_bytes = source_image.read()

    # Our target image: http://i.imgur.com/Xchqm1r.jpg
    with open('target.jpg', 'rb') as target_image:
        target_bytes = target_image.read()

    response = client.compare_faces(
                   SourceImage={ 'Bytes': source_bytes },
                   TargetImage={ 'Bytes': target_bytes },
                   SimilarityThreshold=SIMILARITY_THRESHOLD
    )
    
    print "Similarity", response['FaceMatches'][0]['Similarity']
    if response['FaceMatches'][0]['Similarity'] > 75:
        print "The faces are similar!"
        
print datetime.now() - startTime
