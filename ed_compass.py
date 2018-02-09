import tkinter as tk
from tkinter import ttk
import json

import threading
import time
import json
import math

# init

win = tk.Tk()
win.title("ED-Compass")
#win.iconbitmap('ed.ico')
win.resizable("False", "False")
w = '140'
h = '200'
win.geometry('{}x{}'.format(w, h))

donneeDestinationLatitude = tk.DoubleVar()
donneeDestinationLongitude = tk.DoubleVar()

coordonnesActuelles = ttk.LabelFrame(win, text="Votre position", width="140")
coordonnesActuelles.grid(column=0, row=0)

labelCoordonneesLatitude = ttk.Label(coordonnesActuelles, text="Latitude")
labelCoordonneesLatitude.grid(column=0, row=0, sticky=tk.W)
labelCoordonneesLongitude = ttk.Label(coordonnesActuelles, text="Longitude")
labelCoordonneesLongitude.grid(column=1, row=0, sticky=tk.W)

valueCoordonneesLatitude = ttk.Label(coordonnesActuelles, text="-")
valueCoordonneesLatitude.grid(column=0, row=1, sticky=tk.W)
valueCoordonneesLongitude = ttk.Label(coordonnesActuelles, text="-")
valueCoordonneesLongitude.grid(column=1, row=1, sticky=tk.W)

destination = ttk.LabelFrame(win, text="Votre destination", width="140")
destination.grid(column=0, row=1)

labelDestinationLatitude = ttk.Label(destination, text="Latitude")
labelDestinationLatitude.grid(column=0, row= 0, sticky=tk.W)
labelDestinationLongitude = ttk.Label(destination, text="Longitude")
labelDestinationLongitude.grid(column=1, row= 0, sticky=tk.W)

valueDestinationLatitude = ttk.Entry(destination, width=6,textvariable=donneeDestinationLatitude)
valueDestinationLatitude.grid(column=0, row=1, sticky=tk.W)
valueDestinationLongitude = ttk.Entry(destination, width=6,textvariable=donneeDestinationLongitude)
valueDestinationLongitude.grid(column=1, row=1, sticky=tk.W)

valueDestinationLatitude.focus()

leCap = ttk.LabelFrame(win, text="Cap à suivre", relief="sunken", width="140")
leCap.grid(column=0, row=2)
valueLeCap = ttk.Label(leCap, text="-")
valueLeCap.grid(column=0, row=0)
valueLeCap.configure(font=("Helvetica", "50"))

def refreshPosition(win):
    try:
        with open(r'C:\Users\paind\Saved Games\Frontier Developments\Elite Dangerous\Status.json','r') as infile:
            try:
                status = json.load(infile)
                valueCoordonneesLatitude.config(text=round(status["Latitude"],2))
                valueCoordonneesLongitude.config(text=round(status["Longitude"],2))

                latStart = status["Latitude"] * math.pi/180;
                lonStart = status["Longitude"] * math.pi/180;

                if not latStart:
                    latStart = 0
                if not lonStart:
                    lonStart = 0
                latDest = donneeDestinationLatitude.get() * math.pi/180;
                lonDest = donneeDestinationLongitude.get() * math.pi/180;

                deltaLon = lonDest - lonStart;
                deltaLat = math.log(math.tan(math.pi/4 + latDest/2)/math.tan(math.pi/4 + latStart/2));
                initialBearing = (math.atan2(deltaLon, deltaLat)) * (180/math.pi);

                if initialBearing < 0 :
                    initialBearing = 360 + initialBearing;

                valueLeCap.config(text=round(initialBearing))
            except:
                pass
    except IOError as e:
        print(e)
    else:
        win.after(100, lambda: refreshPosition(win))

refreshPosition(win)
win.mainloop()
