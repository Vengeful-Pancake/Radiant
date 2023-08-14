import cv2
import threading
from system_files.save.save import LOAD
import num
def motion():
    cap = cv2.VideoCapture("c:/temp/Cars - 1900.mp4")

    # create a background object
    backgroundObject = cv2.createBackgroundSubtractorMOG2(history=2)
    kernel = np.ones((3,3),np.uint8)
    kernel2 = None

    while True:
        ret , frame = cap.read()
        if not ret :
            break
        
        fgmask = backgroundObject.apply(frame)
        _, fgmask = cv2.threshold(fgmask ,20 , 255 , cv2.THRESH_BINARY)
        fgmask = cv2.erode(fgmask, kernel, iterations=1)
        fgmask = cv2.dilate(fgmask,kernel2 , iterations=6  )


        # detect the countours
        countors, _ = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        frameCopy = frame.copy()

        # loop inside the countor and search for bigger ones

        for cnt in countors:
            if cv2.contourArea(cnt) > 20000:

                # get the area coordinates
                x , y, width , height = cv2.boundingRect(cnt)

                # draw a rectangle around the area
                cv2.rectangle(frameCopy, (x,y), (x+width, y+ height) , (0,0,255), 2)

                # write a text near the object 
                cv2.putText(frameCopy ,"Car detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3 , (0,255,0), 1, cv2.LINE_AA)

        forground = cv2.bitwise_and(frame,frame , mask = fgmask)

        # combine all together 
        stacked = np.hstack((frame,forground,frameCopy))

        cv2.imshow("stacked", cv2.resize(stacked,None,fx=0.4, fy=0.4))

        #cv2.imshow("forground", forground)
        #cv2.imshow("frameCopy", frameCopy)
        #cv2.imshow("fgmask", fgmask)
        #cv2.imshow("img", frame)

        if cv2.waitKey(1) == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()

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

        frame=cv2.hconcat([frame0,frame1])
        cv2.imshow("Cameras:", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture_0.release()
    video_capture_1.release()
    cv2.destroyAllWindows()