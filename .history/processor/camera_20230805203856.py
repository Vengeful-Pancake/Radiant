import cv2
import threading
from system_files.save import LOAD


class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print "Starting " + self.previewName
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cv2.namedWindow(previewName)
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while rval:
        cv2.imshow(previewName, frame)
        rval, frame = cam.read()
        key = cv2.waitKey(20)
        if key == 27:  # exit on ESC
            break
    cv2.destroyWindow(previewName)
def camera(x,y):
    input1=LOAD("INPUT1","config.txt")
    input1.split(": ")
    input2=LOAD("INPUT2","config.txt")
    input2.split(": ")
    thread1 = camThread(input1[0], input1[0])
    thread2 = camThread(input2[0], input2[0])
    thread1.start()
    thread2.start()