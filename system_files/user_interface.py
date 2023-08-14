import time
import system_files.classes
from processor.camera import camera
from system_files.folders import Browsefolder
from system_files.camera_setting import *
from system_files.save.save import *
from system_files.input_handler import *
from system_files.color import *
from system_files.initial import *

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
            v=1
            y=2
        else:
            v=2 
            y=1
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
                x=str(i)+": "+CAMERANAMES[str(CAMERAINDEXs[i])]
                UIELEMENT("",x,2+i).button()
                if UIELEMENT("",x,2+i).button() == 1:
                    if LOAD("INPUT"+str(v), "config.txt")!=x:
                        SAVE("INPUT"+str(y), x, "config.txt")
                    SAVE("STATE","PROGRAM","config.txt")
        if UIELEMENT("","Cancel", 8).button()==1:
            SAVE("STATE", "PROGRAM", "config.txt")
            CANCEL=1

    if STATE == "3DMODE":
        camera()
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

    