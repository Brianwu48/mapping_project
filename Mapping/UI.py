import os
import classes
import tkinter as tk
from tkintermapview import TkinterMapView as tk_map #pip install tkintermapview
from PIL import Image, ImageTk

name = "Hozio"
address = "405 Lexington Ave\n New York, NY 10174"
priority = 1
category = "SEO"

locations = []
locations.append(classes.pin_location(name, address, priority, category))
locations.append(classes.pin_location("Location 2", "1650 Sycamore Ave\n Bohemia, NY 11716", 3, "SEO")) #This is not needed in final product

win = tk.Tk()

win.geometry("1280x920")
win.title("Google Map Business Tracker")
win.configure(background= '#0F0F0F')

google_map = tk_map(win, width= 1280, height= 720)
google_map.pack_configure(padx= 5, ipadx= 5, pady=20)
google_map.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=17)
google_map.set_position(deg_x=40.2059044, deg_y=-98.5375581)
google_map.set_zoom(5)

current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
pin_green = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "assets", "pin_green.png")).resize((35, 35)))
pin_yellow = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "assets", "pin_yellow.png")).resize((35, 35)))
pin_red = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "assets", "pin_red.png")).resize((35, 35)))
pin_grey = ImageTk.PhotoImage(Image.open(os.path.join(current_path, "assets", "pin_grey.png")).resize((35, 35)))

for pins in locations:
    if(pins.priority == 1):
        current_pin = pin_green
    if(pins.priority == 2):
        current_pin = pin_yellow
    if(pins.priority == 3):
        current_pin = pin_red
    if(pins.priority == 4):
        current_pin = pin_grey

    google_map.set_marker(
        deg_x=pins.latitude,deg_y=pins.longitude,
        text=pins.name+"\n"+
        pins.category+"\n"+
        str(pins.priority), 
        icon=current_pin,
        text_color='black')
    print("Successfully Completed: "+pins.name)
win.mainloop()



