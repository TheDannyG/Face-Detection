# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:13:05 2017

@author: Daniel
"""
#This is a application that when the button is pressed
#the current frame is uploaded to AWS to check if it is a authorized person
#This is the test for the integration of opencv into tkinter so buttons can be used

#import nessisary libraries
import cv2
import Tkinter as tk
from PIL import Image, ImageTk

def show_frame():
    #width, height = 800, 600

    root = tk.Tk()
    lmain = tk.Label(root)
    lmain.pack()
    
    cap = cv2.VideoCapture(0)
    
    def callback():
        print "Authorize"
    
    label = tk.Label(root, text = "Please, press the button to authorize.")
    button = tk.Button(root, text="Authorize", command=callback)
    label.pack(side=tk.RIGHT)
    button.pack(side=tk.RIGHT)
    
    while True:
        ret_val, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        lmain.imgtk = imgtk
        lmain.configure(image=imgtk)
        lmain.after(10, show_frame)

#show_frame()
                
   
#Code to run app
def main():
   show_frame()
   root.mainloop()
if __name__ == '__main__':
    main()