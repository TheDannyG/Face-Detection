# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:06:31 2017

@author: Daniel
"""
import cv2
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