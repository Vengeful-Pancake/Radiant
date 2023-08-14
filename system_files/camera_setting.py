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