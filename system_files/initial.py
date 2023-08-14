import pygame
from system_files.save.save import *
import math
from pygame.locals import *
from win32api import GetMonitorInfo, MonitorFromPoint

monitor_info = GetMonitorInfo(MonitorFromPoint((0,0)))
monitor_area = monitor_info.get("Monitor")
work_area = monitor_info.get("Work")
Taskbar_height = monitor_area[3]-work_area[3]


pygame.init()
type = LOAD("SCREEN", "config.txt")
if type == 1:
    screen = pygame.display.set_mode((900,720)) 
if type == 2:
    screen = pygame.display.set_mode((480,860)) 
if type == 3:
    screen = pygame.display.set_mode((600,940)) 
clock = pygame.time.Clock()

WINDOW_WIDTH, WINDOW_HEIGHT = screen.get_size()
transparency = (255, 0, 128)  
pygame.display.set_caption("2-3D")
font = pygame.font.Font("requires\\coders_crux.ttf", 40)

RUNNING=1
width, height = (900,720)

SAVE("HOLDER","","config.txt")
SAVE("WIDTH", width, "config.txt")
SAVE("BrowseNumber", 1, "config.txt")
SAVE("HEIGHT", height, "config.txt")
SAVE("SCROLL",0, "config.txt")
SAVE("STATE","PROGRAM","config.txt")
SAVE("CAMNAME",{},"config.txt")
SAVE("CAMARRAY",[11],"config.txt")
SAVE("INPUT1","","config.txt")
SAVE("OUTPUT","","config.txt")
SAVE("INPUT2","","config.txt")
SAVE("VIDEO","","config.txt")

bg = pygame.image.load("system_files\\sprite\\infinity.png").convert()
tiles = math.ceil(width / bg.get_width()) + 1
#saved data for cross communication
