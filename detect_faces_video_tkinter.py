import PIL
from PIL import Image,ImageTk
import pytesseract
import cv2
from tkinter import *

detectface=True
detectsmile=True
detecteyes=True

def changestateSmile():
	global detectsmile
	if detectsmile:
		detectsmile=False
	else:
		detectsmile=True
	return detectsmile

def changestateEyes():
	global detecteyes
	if detecteyes:
		detecteyes=False
	else:
		detecteyes=True
	return detecteyes





width, height = 800, 600
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  
smile_cascade=cv2.CascadeClassifier('haarcascade_smile.xml')
root = Tk()
root.bind('<Escape>', lambda e: root.quit())
lmain = Label(root)
lmain.pack()



button = Button(master=root, text='smile', command= lambda: changestateSmile())
button.pack()

button1 = Button(master=root, text='eyes', command= lambda: changestateEyes())
button1.pack()

def show_frame():

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
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 7)  
  
        #To draw a rectangle in eyes 
        for (ex,ey,ew,eh) in eyes:
        	if detecteyes:
        		cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2) 

        smile = smile_cascade.detectMultiScale(
            roi_gray,
            scaleFactor=1.3,
            minNeighbors=15,
            minSize=(15, 15),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in smile:
        	if detectsmile:
        		cv2.rectangle(roi_color, (x, y), (x + w, y + h), (0, 0, 255), 1)


    cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    img = PIL.Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)
    print(detectsmile)

show_frame()
root.mainloop()