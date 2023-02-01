import tkinter
import cv2
import PIL.Image, PIL.ImageTk
from functools import partial
import threading
import time
import imutils

stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"You clicked on Play. Speed is {speed}")

 # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    if flag:
        canvas.create_text(134, 26, fill="white", font="Times 30 italics bold", text="Decision Pending")
    flag = not flag
    
def pending(decision):
    #1. Display decision pending image
    frame = cv2.cvtColor(cv2.imread("Dp.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    
    #2. wait for 1 second
    time.sleep(1.5)
    
    #3. display sponsor image
    frame = cv2.cvtColor(cv2.imread("sponsor.jpg"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
   
    #4. wait for 1.5 second
    time.sleep(2.5)
    
    #5. Display out/notout image
    if decision == 'out':
            decisionImg = "out.jpg"
    else:
        decisionImg = "No.jpg"
    frame = cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width=SET_WIDTH, height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    
    pass 
   
def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("player is out")
    
def Not_Out():
    thread = threading.Thread(target=pending, args=(" Not out",))
    thread.daemon = 1
    thread.start()
    print("player is Not out")        
    
SET_WIDTH = 500
SET_HEIGHT = 316

window = tkinter.Tk()
window.title("Third Umpire Decision Review Kit")
cv_img = cv2.cvtColor(cv2.imread("welcome.jpg"), cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, ancho=tkinter.NW, image=photo)
canvas.pack()


#buttons to control playback
btn = tkinter.Button(window,text="<< previous (fast)", width=50, command=partial(play, -20))
btn.pack()

btn = tkinter.Button(window,text="<< previous (slow)", width=50, command=partial(play, -4))
btn.pack()

btn = tkinter.Button(window,text=" Next (fast) >>", width=50, command=partial(play, 30))
btn.pack()

btn = tkinter.Button(window,text=" Next (slow) >>", width=50, command=partial(play, 4))
btn.pack()

btn = tkinter.Button(window,text=" Out", width=50, command=out)
btn.pack()

btn = tkinter.Button(window,text=" Not Out", width=50, command=Not_Out)
btn.pack()
window.mainloop()

