#
#
#       Key-Holding-Macro made by JngVedere
#       Github : https://github.com/JngVedere
#       version 0.1.0 - Released on 03-06-2023
#
#

from tkinter import messagebox, ttk
from tendo import singleton
try:
    singleton.SingleInstance()
except SystemExit as e:
    messagebox.showerror("ERROR", e)

import tkinter as tk
import pywinauto, XK_TO_DD
import threading
from time import sleep

try:
    from KeyHolding import KeyToWindow, getKeyPressing
    from KeyHolding import wnd_check_thread

except SystemExit as e:
    messagebox.showerror("ERROR",e)
    exit(0)

# // Global variables
root:object = tk.Tk()
app:object
app_title:str = "Key Holding Macro"
app_size:tuple = (350,170)
window_info:str = ""
simplified:bool = True

# // GUI
class MainApp:
    
    def __init__(self, master):
        global simplified

        # Basic Variables
        self.master = master
        self.key_pressed = False
        self.key_to_send = -1

        #Frame
        self.master.title(app_title)
        self.X = int(self.master.winfo_screenwidth()/2 - app_size[0]/2)
        self.Y = int(self.master.winfo_screenheight()/2 - app_size[1]/2)
        self.master.wm_geometry(f"{app_size[0]}x{app_size[1]}+{self.X}+{self.Y}")
        self.master.minsize(250, 150)
        self.master.maxsize(700, 220)
        self.master.resizable(True,False)
        self.master.bind("<Key>", self.key_press)

        self.upper_frame = tk.Frame(width=100, relief="sunken",bd=1)
        self.upper_frame.pack(side="top",fill="both",padx=5,ipadx=2,pady=5,ipady=2)
        self.lower_frame = tk.Frame(width=100, height=110, relief="sunken",bd=1)
        self.lower_frame.pack(side="bottom",fill="both",padx=5,ipadx=2,pady=5,ipady=2,expand=True)

        self.window_combobox = ttk.Combobox(self.upper_frame, width = 40, postcommand = lambda:self.update_cb_list(simplified), state='readonly')
        self.window_combobox.set("Pick a Window")
        self.window_combobox.pack(fill="x",padx=3,pady=3,side="top")
        self.window_combobox.bind("<<ComboboxSelected>>",self.window_selected)

        self.check_var = tk.BooleanVar(value=True)
        self.simplified_checkbutton = tk.Checkbutton(self.upper_frame, text='Simplified Window', variable=self.check_var, onvalue=True, offvalue=False, command=self.on_check_button_click)
        # self.simplified_checkbutton.bind("<ButtonRelease-1>",self.on_check_button_click)
        self.simplified_checkbutton.pack(pady=2)
        print(self.check_var.get())

        self.show_key = tk.Label(self.lower_frame, text="<Press any key to hold>", bg='gray19', fg='snow')
        self.show_key.pack(pady=5)

        self.send_button = tk.Button(self.lower_frame, text="Hold Key", command=self.button_pressed, takefocus=False)
        self.send_button.pack(pady=3)

        self.ro_textbox = ttk.Label(self.lower_frame, text='',border=1,font=("Calibri",12,"bold"))
        self.ro_textbox.pack(side="bottom")

    def update_cb_list(self, simplified):
        print("updt cb list", simplified)
        if simplified == True: # Find window by window name
            self.temp_list = pywinauto.Desktop(backend='uia').windows(title_re ='.')
            self.values_list = [w.window_text() for w in self.temp_list]

        else: # Find window by hwnd
            self.values_list = []
            self.hwnd_list = []
            procs = pywinauto.findwindows.find_elements()
            for proc in procs:
                self.hwnd_list.append(proc.handle)
                self.values_list.append((proc.name,proc.class_name))   

        self.window_combobox['value'] = self.values_list
    
    def on_check_button_click(self):
        def update_check_var(): #To Avoid Firing two functional works
            print("Button Clicked")
            global simplified
            simplified = self.check_var.get()
            self.window_combobox.set("Pick a Window")
            print(self.check_var.get())

        self.master.after(30, update_check_var)

    def window_selected(self, event):
        global window_info
        if simplified == True:
            window_info = self.window_combobox.get()
        elif simplified == False:
            window_info = self.hwnd_list[self.window_combobox.current()]

    def key_press(self, event):
        if self.key_pressed == False:
            self.show_key.config(text=event.keysym)
            self.key_to_send = XK_TO_DD.XK_TO_DD[str(event.keycode)]
            print(repr(event.char), repr(event.keysym), repr(event.keycode), repr(event.keysym_num))

    def button_pressed(self):
        global window_info
        
        if self.window_combobox.current() == -1:
            messagebox.showerror("ERROR", "Window isn't selected")  
            return
        
        elif self.key_to_send == -1:
            messagebox.showerror("ERROR", "Key isn't selected")
            return

        if not KeyToWindow.is_valid_window_info(window_info): return
        print(window_info)

        if not self.key_pressed:
            self.activate_button()
                         
        else:
            self.deactivate_button()
    
    def SafeQuit(self, master:object = root) -> None:
        if messagebox.askokcancel(f"{app_title} Quit", f"Are you sure that you want to quit {app_title}?"):
            if getKeyPressing() == True:
                KeyToWindow.send_key_to_window(window_info, self.key_to_send, key_down=False)
                print("Events Listening is stopped!")
            master.destroy()

    def is_input_activating(self):

        if getKeyPressing() == True:
            self.ro_textbox.config(text='Activating')
        else:
            self.ro_textbox.config(text='Not Activating')

        self.is_hwnd_available()
        
    def is_hwnd_available(self):
        global window_info

        if not KeyToWindow.is_valid_window_info(window_info):
            self.deactivate_button()

    def activate_button(self):
        global window_info

        KeyToWindow.send_key_to_window(window_info, self.key_to_send, key_down=True)
        self.key_pressed = True
        wnd_check_thread.resume()
        key_check_thread.resume()
        self.window_combobox.config(state='disabled')
        self.simplified_checkbutton.config(state='disabled')
        self.ro_textbox.config(text='')
        self.send_button.config(text="Release Key")
    
    def deactivate_button(self):
        global window_info

        KeyToWindow.send_key_to_window(window_info, self.key_to_send, key_down=False)
        self.key_pressed = False
        wnd_check_thread.pause()
        key_check_thread.pause()
        self.window_combobox.config(state='normal')
        self.simplified_checkbutton.config(state='normal')
        self.ro_textbox.config(text='')
        self.send_button.config(text="Hold Key")

#// Logics Threading
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
            app.is_input_activating()
            # Wait for a short time before checking again
            sleep(0.1)

    def pause(self):
        self.pause_event.clear()

    def resume(self):
        self.pause_event.set()

if __name__ == "__main__":
    app = MainApp(root)
    key_check_thread = MyThread()
    key_check_thread.start()
    root.protocol("WM_DELETE_WINDOW", app.SafeQuit)
    root.mainloop()