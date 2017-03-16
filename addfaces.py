# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 17:10:29 2017

@author: Daniel
"""
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
import Tkinter as tk
#Import the search_face program's function to find faces and compare them
#to the faces in the cloud
#This file must be in the same directory as index_face
from index_faces import index_face

#Connect to AWS
client = boto3.client('rekognition')

#Set collection name for the to put the face in
collection_name = 'authorized_faces'

#Define what a switch is, for the trach bar that will act as a button
switch = '0 : OFF \n1 : ON'

#Define the action that will happen when the track bar is switched
#It will take the current frame call hte index_face function
def Empty(x):
    #Empty function for the trackbar
    return x   
#Define the function that creates the window and displays webcam output
def show_webcam(mirror=False):  
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
            #create the windows
            root = tk.Tk()
            def callback():
                name = entry.get()
                print name
                
                root.destroy()
                
                face_name = name
                face_num = index_face(client, cv2.imencode('.jpg', img)[1].tostring(), collection_name, face_name)
                print "Done"
                
            label = tk.Label(root, text = "Type in the name of the person to be added.")
            entry = tk.Entry(root)
            button = tk.Button(root, text="OK", command=callback)
            label.pack(side=tk.TOP)
            entry.pack()
            button.pack()
            
            
            
            
            tk.mainloop()
        #Disply the video feed
        cv2.imshow('Face Authorizer', img)
        
    #Close windows when loop is finshed
    cv2.destroyAllWindows()

#Code to run app
def main():
   show_webcam(mirror=True)
if __name__ == '__main__':
    main()
