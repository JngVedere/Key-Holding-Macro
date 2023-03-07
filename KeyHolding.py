#
#
#       KeyHolding.py written by JngVedere
#       Github : https://github.com/JngVedere
#       version 0.1.0 - Released on 03-06-2023
#
#

import win32gui
import ctypes
import os
import threading
from time import sleep
from tkinter import messagebox

# // Global variables
key_pressing:bool = False
target_key:int = 0
hwnd:int = 0
last_active_window = None

# // ClasDD init
try:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    dd_dll = ctypes.windll.LoadLibrary(dir_path + '//DD94687.64.dll')
    st = dd_dll.DD_btn(0) # classDD init
except:
    raise SystemExit("DD94687.64.dll Not Found")

if st==1:
    print('ClassDD Ready')
else:
    print('ERROR')
    raise SystemExit("DD94687.64.dll Not Imported")

# // Logics send key to window
class KeyToWindow:

    @staticmethod
    def send_key_to_window(window_info, key:int, key_down = False):  
        global hwnd, key_pressing,target_key, wnd_check_thread

        # Check window_info is 'hwnd' or 'window name'
        if isinstance(window_info, int): # if window_info is hwnd(int) value
            hwnd = window_info
        elif window_info.isdigit(): # if window_info is hwnd(str) value
            hwnd = int(window_info)
        else: # if window_info is window_name(str) value
            hwnd = win32gui.FindWindow(None, window_info)
        
        if not KeyToWindow.is_valid_hwnd(hwnd): return

        #Key pressing process
        target_key = key
        
        if key_down == True:
            if key_pressing == False:
                key_pressing = True
                dd_dll.DD_key(target_key,1) #DD_key(#_key, 1 for keydown/2 for keyUp)
                print("keyDown", key_pressing)
                return True
            
        elif key_down == False:
            if key_pressing == True:
                key_pressing = False
                dd_dll.DD_key(target_key,2)
                print("keyUp", key_pressing)
                return False
    
    @staticmethod
    def send_key(is_active):
        KeyToWindow.send_key_to_window(hwnd, target_key,key_down=is_active)

    @staticmethod
    def is_valid_hwnd(hwnd) -> bool:
        # ERROR case
        if not win32gui.IsWindow(hwnd):
            messagebox.showerror("ERROR","Window not found")

            return False
        
        return True
    
    @staticmethod
    def is_valid_window_info(window_info) -> bool:
        temp_hwnd = ''

        # Check window_info is 'hwnd' or 'window name'
        if isinstance(window_info, int): # if window_info is hwnd(int) value
            temp_hwnd = window_info
        elif window_info.isdigit(): # if window_info is hwnd(str) value
            temp_hwnd = int(window_info)
        else: # if window_info is window_name(str) value
            temp_hwnd = win32gui.FindWindow(None, window_info)
        
        return KeyToWindow.is_valid_hwnd(temp_hwnd)
    
# // Operations for checking window switched
class WindowActiveChecker:
    global hwnd

    @staticmethod
    def is_target_active(active_window):      
        KeyToWindow.send_key(hwnd == active_window)

    @staticmethod
    def detect_window_switch():
        global last_active_window

        # Loop indefinitely
        # Get the active window handle
        active_window = win32gui.GetForegroundWindow()

        # If the active window is different from the last active window
        if active_window != last_active_window:
            # Check active window is target window
            WindowActiveChecker.is_target_active(active_window)

            # # Get the window text
            # window_text = win32gui.GetWindowText(active_window)
            
            # # Print the window text and window class
            # print("Window switched: %s (%s)" % (window_text, win32gui.GetClassName(active_window)))

            # Set the last active window to the current active window
            last_active_window = active_window 

# // Logics Threading
class MyThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.pause_event = threading.Event()
        self.pause_event.clear()
        self.daemon = True

    def run(self):
        # while not self.pause_event.is_set():
        while True:
            self.pause_event.wait()
            WindowActiveChecker.detect_window_switch()
            # Wait for a short time before checking again
            sleep(0.1)

    def pause(self):
        self.pause_event.clear()

    def resume(self):
        self.pause_event.set()

def getKeyPressing() -> bool:
    global key_pressing
    return key_pressing

if __name__ != '__main__':
    wnd_check_thread = MyThread()
    sleep(0.1)
    wnd_check_thread.start()
