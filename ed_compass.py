import tkinter as tk
from tkinter import ttk
import json

import threading
import time
import json
import math

# init

win = tk.Tk()
win.title("D'où que je vais")
win.iconbitmap('ed.ico')
win.resizable("False", "False")

donneeDestinationLatitude = tk.DoubleVar()
donneeDestinationLongitude = tk.DoubleVar()

coordonnesActuelles = ttk.LabelFrame(win, text="Votre position actuelle")
coordonnesActuelles.grid(column=0, row=0)

labelCoordonneesLatitude = ttk.Label(coordonnesActuelles, text="Latitude").grid(column=0, row= 0, sticky=tk.W)
labelCoordonneesLongitude = ttk.Label(coordonnesActuelles, text="Longitude").grid(column=1, row= 0, sticky=tk.W)
labelCoordonneesAltitude = ttk.Label(coordonnesActuelles, text="Altitude").grid(column=2, row= 0, sticky=tk.W)

valueCoordonneesLatitude = ttk.Label(coordonnesActuelles, text="-")
valueCoordonneesLatitude.grid(column=0, row=1, sticky=tk.W)
valueCoordonneesLongitude = ttk.Label(coordonnesActuelles, text="-")
valueCoordonneesLongitude.grid(column=1, row=1, sticky=tk.W)
valueCoordonneesAltitude = ttk.Label(coordonnesActuelles, text="-")
valueCoordonneesAltitude.grid(column=2, row=1, sticky=tk.W)

leCap = ttk.LabelFrame(win, text="Cap à suivre")
leCap.grid(column=0, row=1)
labelCoordonneesCap = ttk.Label(leCap, text="Actuel")
labelCoordonneesCap.grid(column=0, row=0, sticky=tk.W)
valueCoordonneesCap = ttk.Label(leCap, text="-")
valueCoordonneesCap.grid(column=0, row=1, sticky=tk.W)
labelLeCap = ttk.Label(leCap, text="Vers destination")
labelLeCap.grid(column=1, row=0, sticky=tk.W)
valueLeCap = ttk.Label(leCap, text="-")
valueLeCap.grid(column=2, row=1, sticky=tk.W)

destination = ttk.LabelFrame(win, text="Votre destination souhaitée")
destination.grid(column=0, row=2)

labelDestinationLatitude = ttk.Label(destination, text="Latitude").grid(column=0, row= 0, sticky=tk.W)
labelDestinationLongitude = ttk.Label(destination, text="Longitude").grid(column=1, row= 0, sticky=tk.W)

valueDestinationLatitude = ttk.Entry(destination, width=6,textvariable=donneeDestinationLatitude)
valueDestinationLatitude.grid(column=0, row=1, sticky=tk.W)
valueDestinationLongitude = ttk.Entry(destination, width=6,textvariable=donneeDestinationLongitude).grid(column=1, row=1, sticky=tk.W)

valueDestinationLatitude.focus()

def refreshPosition(win):
    try:
        with open(r'C:\Users\paind\Saved Games\Frontier Developments\Elite Dangerous\Status.json','r') as infile:
            try:
                status = json.load(infile)
                valueCoordonneesLatitude.config(text=status["Latitude"])
                valueCoordonneesLongitude.config(text=status["Longitude"])
                valueCoordonneesAltitude.config(text=status["Altitude"])
                valueCoordonneesCap.config(text=status["Heading"])

                latStart = status["Latitude"] * math.pi/180;
                lonStart = status["Longitude"] * math.pi/180;
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
