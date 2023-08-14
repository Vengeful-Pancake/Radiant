from system_files.save.save import *
from system_files.input_handler import *
from system_files.color import *
from system_files.initial import *
import time
import tkinter
from tkinter import filedialog
import os
import cv2
from pygrabber.dshow_graph import FilterGraph

def namecams():
    devices = FilterGraph().get_input_devices()
    availablecameras = {}
    for device_index, device_name in enumerate(devices):
        availablecameras[device_index]=device_name
    return availablecameras


def availcams():
    arr = []
    for i in range(10):
        cap=cv2.VideoCapture(i)
        if cap.read() [0]:
            arr.append(i)
        cap.release()
    
    return arr

def Browsefolder(file):
    root = tkinter.Tk()
    root.withdraw() #use to hide tkinter window
    if file:
        filename = filedialog.askopenfilename(
        filetypes=(
            ("MP4 files", "*.mp4"),
            ("Python Files", ("*.py", "*.pyx")),
            ("All Files", "*.*")
        ))
        return filename
    
    currdir = os.getcwd()
    tempdir = filedialog.askdirectory(parent=root, initialdir=currdir, title='Please select a directory')
    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
    file_path_variable = tempdir
    print ("\nfile_path_variable = ", file_path_variable)
    return str(file_path_variable)

def scroller():
    x=LOAD("SCROLL", "config.txt")
    w=LOAD("WIDTH", "config.txt")
    xx=bg.get_width()
    if((xx-x)<w):
        screen.blit(bg,(xx-x,0))
    screen.blit(bg, (-x,0))
    
    if (xx==x):
        x=-1
    SAVE("SCROLL",x+1, "config.txt")

class UIELEMENT:
    def __init__(self, object, string, pos):
        self.object = object
        self.rawstring=string
        self.pos = pos
        self.w=LOAD("WIDTH", "config.txt")
        self.h=LOAD("HEIGHT", "config.txt")
        self.string = font.render(string, True, black)
        self.str=self.string.get_size()
        self.x1=self.w/2-self.str[0]/2-5
        self.x2=self.w/2-self.str[0]/2-5+self.str[0]+10
        self.y1=self.h/9*(self.pos-1)-self.str[1]/2+5+20
        self.y2=self.h/9*(self.pos-1)-self.str[1]/2+5+self.str[1]+10+20
        if self.object=="mode":
            self.x1=self.w-self.str[0]-25
            self.x2=self.w-10
            self.y1=10
            self.y2=self.str[1]+10+10
        left, middle, right = pygame.mouse.get_pressed()
        mouse= mouse_position()
        if self.x1<mouse[0]<self.x2 and self.y1<mouse[1]<self.y2:
            self.state="hover"
            if left:
                self.state="click"
        else: 
            self.state="idle"
        if self.state == "idle":
            self.color = black
            self.colorx = blue
            self.colory = red
        else:
            self.color = grey
            self.colorx = light_blue
            self.colory = light_red
        self.string = font.render(string, True, self.color)
    
    def button(self):
        pygame.draw.rect(screen,self.colorx, pygame.Rect(self.x1, self.y1, self.str[0]+10, self.str[1]+10))
        pygame.draw.rect(screen,self.colory, pygame.Rect(self.x1, self.y1, self.str[0]+10, self.str[1]+10),2)
        screen.blit(self.string, (self.w/2-self.str[0]/2,self.h/9*(self.pos-1)+20))
        if self.state=="click":
            return 1
        return 0
    
    def text(self):
        string = font.render(self.rawstring, True, black)
        screen.blit(string, (20,20+self.h/9*(self.pos-1)))
    
    def mode(self):
        pygame.draw.rect(screen,self.colorx, pygame.Rect(self.x1, self.y1, self.str[0]+10, self.str[1]+10))
        pygame.draw.rect(screen,self.colory, pygame.Rect(self.x1, self.y1, self.str[0]+10, self.str[1]+10),2)
        screen.blit(self.string, (self.w-self.str[0]-20,20))
        if self.state=="click":
            return 1
        return 0
        
def screen_display():
    STATE=LOAD("STATE","config.txt")
    screen.fill(black)
    MODE = LOAD("MODE", "config.txt")
    scroller()
    if STATE == "PROGRAM":
        
        UIELEMENT("","Input:",1).text()
        UIELEMENT("","Output:",5).text()
        if (MODE=="CAMERA"):
            UIELEMENT("", LOAD("INPUT1", "config.txt"),2).text()
            UIELEMENT("", LOAD("INPUT2", "config.txt"),3).text()
        if (MODE=="VIDEO"):
            UIELEMENT("", LOAD("VIDEO", "config.txt"),2).text()
        UIELEMENT("", LOAD("OUTPUT", "config.txt"),6).text()
        if(LOAD("MODE", "config.txt")=="VIDEO"):
            Browse="Browse Input Video"
        elif(LOAD("BrowseNumber", "config.txt")==1):
            Browse="Browse Input 1"
        else:
            Browse="Browse Input 2"

        UIELEMENT("", Browse, 4).button()
        UIELEMENT("", "Browse",7).button()
        UIELEMENT("", "Process",8).button()
        UIELEMENT("", "View",9).button()
        UIELEMENT("mode",MODE,0).mode()

        if UIELEMENT("", Browse, 4).button()==1:
            print("BROWSE INPUT")
            if(LOAD("MODE", "config.txt")=="VIDEO"):
                print ("Browse Input Video")
                SAVE("VIDEO", Browsefolder(1), "config.txt")
            elif(LOAD("BrowseNumber", "config.txt")==1):
                SAVE("BrowseNumber", 2, "config.txt")
                SAVE("STATE","CAMERA","config.txt")                    
            else:
                SAVE("BrowseNumber", 1, "config.txt")
                SAVE("STATE","CAMERA","config.txt")
        elif UIELEMENT("", "Browse",7).button() == 1:
            print("BROWSE OUTPUT")
            SAVE("OUTPUT", Browsefolder(0),"config.txt")
        elif UIELEMENT("", "Process",8).button() == 1:
            print("PROCESSING...")
            SAVE("STATE","3DMODE","config.txt")
        elif UIELEMENT("", "View",9).button() == 1:
            print("VIEW PROCESSED FILE")
            SAVE("STATE","VIEW","config.txt")
        elif UIELEMENT("mode",MODE,0).mode() == 1:
            print("change mode")
            if (MODE=="CAMERA"):
                SAVE("MODE","VIDEO","config.txt")
                time.sleep(0.1)
            if (MODE=="VIDEO"):
                SAVE("MODE","CAMERA","config.txt")
                time.sleep(0.1)

    if STATE == "CAMERA":
        UIELEMENT("", "Detected cameras:------------",1).text()
        UIELEMENT("","Cancel", 8).button()
        CAMERANAMES = LOAD("CAMNAME","config.txt")
        CAMERAINDEXs = LOAD("CAMARRAY","config.txt")
        if LOAD("BrowseNumber","config.txt") == 1:
            y=2
        else: y=1
        if (CAMERAINDEXs[0]==11):
            try:
                CAMERANAMES = namecams()
                CAMERAINDEXs = availcams()
                SAVE("CAMNAME",CAMERANAMES,"config.txt")
                SAVE("CAMARRAY",CAMERAINDEXs,"config.txt")
            except:
                print("NO INPUT CAMERA...")
                SAVE("CAMARRAY",[12],"config.txt")
        CAMERANAMES = LOAD("CAMNAME","config.txt")
        CAMERAINDEXs = LOAD("CAMARRAY","config.txt")

        if (CAMERAINDEXs[0]!=11) and (CAMERAINDEXs[0]!=12):
            for i in range(len(CAMERAINDEXs)):
                x=str(i)+": "CAMERANAMES[str(CAMERAINDEXs[i])]
                UIELEMENT("",x,2+i).button()
                if UIELEMENT("",x,2+i).button() == 1:
                    SAVE("INPUT"+str(y), x, "config.txt")
                    SAVE("STATE","PROGRAM","config.txt")
        if UIELEMENT("","Cancel", 8).button()==1:
            SAVE("STATE", "PROGRAM", "config.txt")
            CANCEL=1

    if STATE == "3DMODE":
        time.sleep(1)
        SAVE("STATE", "PROGRAM","config.txt")
    
    if STATE == "VIEW":
        time.sleep(1)
        SAVE("STATE", "PROGRAM","config.txt")
    
    pygame.display.flip()
    clock.tick(30)



def UI(INPUT_HOLDER):
    HOLDER=LOAD("HOLDER","config.txt")
    SCREEN = LOAD('SCREEN',"config.txt")
    USER_INPUT=input(SCREEN)
    if USER_INPUT != "null" and USER_INPUT != INPUT_HOLDER:
        print (USER_INPUT)

    if USER_INPUT == "F11":
        if SCREEN<3:
            SCREEN+=1
        else:
            SCREEN=1
        SAVE("SCREEN",SCREEN,"config.txt")
    INPUT_HOLDER=USER_INPUT
    screen_display()

    