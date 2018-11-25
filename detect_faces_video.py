# OpenCV program to detect face in real time 

import cv2  
import tkinter as tk
# load the required trained XML classifiers 
# https://github.com/Itseez/opencv
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
cv2.namedWindow("webcam")  
# capture frames from a camera 
cap = cv2.VideoCapture(0) 
cap.set(3,640)
cap.set(4,480)
# loop runs if capturing has been initialized. 
while 1:  
    fps = int(cap.get(5))
    print(fps)
    # reads frames from a camera 
    ret, img = cap.read()  
  
    # convert to gray scale of each frames 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
    # Detects faces of different sizes in the input image 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
  
    for (x,y,w,h) in faces: 
        # To draw a rectangle in a face  
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        roi_gray = gray[y:y+h, x:x+w] 
        roi_color = img[y:y+h, x:x+w] 
  
        # Detects eyes of different sizes in the input image 
        eyes = eye_cascade.detectMultiScale(roi_gray)  
  
        #To draw a rectangle in eyes 
        for (ex,ey,ew,eh) in eyes: 
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2) 

        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.3,
            minNeighbors=5,
            minSize=(25, 25),
            flags=cv2.CASCADE_SCALE_IMAGE
        )

        # Set region of interest for smiles
        for (x, y, w, h) in smile:
            cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 0, 255), 1)
  

    # Display an image in a window 
    cv2.imshow('webcam',img) 
  
    # Wait for Esc key to stop 
    k = cv2.waitKey(30) & 0xff
    if k == 27: 
        break
  
# Close the window 
cap.release() 
  
# De-allocate any associated memory usage 
cv2.destroyAllWindows()  