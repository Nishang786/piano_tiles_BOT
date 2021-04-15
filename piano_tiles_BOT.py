import pyautogui 
import time
from mss import mss 

start_x = 726
start_y = 571
bbox = (start_x , start_y, start_x + 480, start_y + 1 )
cord_x = [ 0, 160, 320, 479]

def test_time():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
              img = sct.grab(sct.monitors[1])
    t2 = time.time()
    print(t2-t1)

def mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)
       

def start():
    while True:
        with mss() as sct:
           img = sct.grab(bbox)
           for cord in cord_x:
               if img.pixel(cord, 0) [0] < 100:
                   pyautogui.click(start_x + cord, start_y)
                   break 
start()
           