# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 13:13:13 2017

@author: Daniel
"""

#This is a application that when the switch trackbar is switched
#the current frame is uploaded to AWS to check if it is a authorized person

#import nessisary libraries
import cv2
import boto3
import time
#Import the search_face program's function to find faces and compare them
#to the faces in the cloud
#This file must be in the same directory as search_face
from search_faces import search_face

#Connect to AWS
client = boto3.client('rekognition')

#Set collection name for the search_face
collection_name = 'authorized_faces'
#Set the the threshhold to be considered a match
match_threshold = 0.85

#Define what a switch is, for the trach bar that will act as a button
switch = '0 : OFF \n1 : ON'

#Define the action that will happen when the track bar is switched
#It will take the current frame and call the search_face function to find
#faces and return the output
def Empty(x):
    #Empty function for the trackbar
    return x
    
#Define the function that creates the window and displays webcam output
def show_webcam(mirror=False):
    startTime = 0
    
    #Define font
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    #Define variable that holds authrization level
    authorized = ''
    
    #Define empty face variable
    face_name = ''
    #Name the window
    cv2.namedWindow('Face Authorizer')
    #Start video capture
    cam = cv2.VideoCapture(0)
    
    #Main loop
    while True:
        ret_val, img = cam.read()
        
        #Create trackbar
        cv2.createTrackbar(switch, 'Face Authorizer',0,1,Empty)
        
        #esc to quit
        if cv2.waitKey(1) == 27: 
            break  
    
            #Mirror webcam feed so it is like looking in a mirror
        if mirror: 
            img = cv2.flip(img, 1)
        
        #Get trackbar posiotion
        s = cv2.getTrackbarPos(switch,'Face Authorizer')
        
        #If pressed:
        if s == 1:
            #Check for faces using search_face function and out who it finds
            face_name = search_face(client, cv2.imencode('.jpg', img)[1].tostring(), collection_name, match_threshold)
                        
            s = "";
                                 
            #Checks if they are authorized
            if face_name == "UNKNOWN":
                seq = (face_name, ": ", "Not Authorized") 
                authorized = s.join(seq) 
                print authorized
                startTime = time.time()
            else:
                seq = (face_name, ": ", "Authorized")   
                authorized = s.join(seq)
                print authorized
                #check time
                startTime = time.time()

        if (startTime >= time.time()-5) & (startTime <= time.time()):
            #Display the who is currently detected and authrization level
            cv2.putText(img,authorized,(10,30), font, 1,(0,255,0),2)
        
        #Disply the video feed
        cv2.imshow('Face Authorizer', img)
        
    #Close windows when loop is finshed
    cv2.destroyAllWindows()

#Code to run app
def main():
   show_webcam(mirror=True)
if __name__ == '__main__':
    main()