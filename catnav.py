import tkinter as tk
from tkinter import ttk

import threading
import time
import json
import math
import os

import ctypes

#   shortcuts to the WinAPI functionality
set_window_pos = ctypes.windll.user32.SetWindowPos
get_window_long = ctypes.windll.user32.GetWindowLongW
set_window_long = ctypes.windll.user32.SetWindowLongW
get_parent = ctypes.windll.user32.GetParent
#   some of the WinAPI flags
GWL_STYLE = -16
GWL_EXSTYLE = -20
WS_MINIMIZEBOX = 131072
WS_MAXIMIZEBOX = 65536
SWP_NOZORDER = 4
SWP_NOMOVE = 2
SWP_NOSIZE = 1
SWP_FRAMECHANGED = 32
WS_EX_APPWINDOW  = 0x00040000
WS_EX_LAYERED    = 0x00080000

from pathlib import Path
home = str(Path.home())

PATH_EDSTATUS_DEFAULT = os.path.join (
    home, "Saved Games","Frontier Developments","Elite Dangerous","Status.json"
)

# init
win = tk.Tk()
win.title("CatNav")
win.iconbitmap('ed.ico')
win.resizable("False", "False")
win.geometry("130x190")

hwnd = get_parent(win.winfo_id())
old_style = get_window_long(hwnd, GWL_STYLE)
new_style = old_style & ~ WS_MAXIMIZEBOX & ~ WS_MINIMIZEBOX
set_window_long(hwnd, GWL_STYLE, new_style)
set_window_pos(hwnd, 0, 0, 0, 0, 0, SWP_NOMOVE | SWP_NOSIZE | SWP_NOZORDER | SWP_FRAMECHANGED)

donneeDestinationLatitude = tk.DoubleVar()
donneeDestinationLongitude = tk.DoubleVar()

destination = ttk.LabelFrame(win, text="Your destination")
destination.pack(fill="x")
destination.columnconfigure(0, weight=1)

labelDestinationLatitude = ttk.Label(destination, text="  Latitude  ")
labelDestinationLatitude.grid(column=0, row= 0, sticky=tk.N)
labelDestinationLongitude = ttk.Label(destination, text="  Longitude  ")
labelDestinationLongitude.grid(column=1, row= 0, sticky=tk.N)

valueDestinationLatitude = ttk.Entry(destination, width=6,textvariable=donneeDestinationLatitude)
valueDestinationLatitude.grid(column=0, row=1, sticky=tk.N)
valueDestinationLongitude = ttk.Entry(destination, width=6,textvariable=donneeDestinationLongitude)
valueDestinationLongitude.grid(column=1, row=1, sticky=tk.N)

valueDestinationLatitude.focus()

leCap = ttk.LabelFrame(win, text="", relief="sunken")
leCap.columnconfigure(0, weight=1)
leCap.pack(fill="x")
valueLeCap = ttk.Label(leCap, text="-")
valueLeCap.grid(column=0, row=0, sticky=tk.N)
valueLeCap.configure(font=("Helvetica", "52"))
valueLeCap.columnconfigure(0, weight=1)

def refreshPosition(win):
    try:
        with open(PATH_EDSTATUS_DEFAULT,'r') as infile:
            try:
                status = json.load(infile)

                latStart = status["Latitude"] * math.pi/180
                lonStart = status["Longitude"] * math.pi/180

                if not latStart:
                    latStart = 0
                if not lonStart:
                    lonStart = 0

                latDest = donneeDestinationLatitude.get() * math.pi/180
                lonDest = donneeDestinationLongitude.get() * math.pi/180

                deltaLon = lonDest - lonStart
                deltaLat = math.log(math.tan(math.pi/4 + latDest/2)/math.tan(math.pi/4 + latStart/2))
                initialBearing = (math.atan2(deltaLon, deltaLat)) * (180/math.pi);

                if initialBearing < 0 :
                    initialBearing = 360 + initialBearing

                valueLeCap.config(text=round(initialBearing))
            except:
                pass
    except:
        pass
    else:
        win.after(400, lambda: refreshPosition(win))

refreshPosition(win)
win.mainloop()
