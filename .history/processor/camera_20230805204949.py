import cv2
import threading
from system_files.save.save import LOAD


class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print ("Starting " + self.previewName)
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

def camera():
    input1=LOAD("INPUT1","config.txt")
    input1.split(": ")
    input2=LOAD("INPUT2","config.txt")
    input2.split(": ")
    # thread1 = camThread(input1[1], int(input1[0]))
    # thread2 = camThread(input2[1], int(input2[0]))
    # thread1.start()
    # thread2.start()
    video_capture_0 = cv2.VideoCapture(int(input1[0]))
    video_capture_1 = cv2.VideoCapture(int(input2[0]))

    while True:
        # Capture frame-by-frame
        ret0, frame0 = video_capture_0.read()
        ret1, frame1 = video_capture_1.read()

        if (ret0):
            # Display the resulting frame
            cv2.imshow(input1[1], frame0)

        if (ret1):
            # Display the resulting frame
            cv2.imshow(input2[1], frame1)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture_0.release()
    video_capture_1.release()
    cv2.destroyAllWindows()