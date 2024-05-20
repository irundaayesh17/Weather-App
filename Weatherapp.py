import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk

#api fetching



#functions



#creating the GUI

weatherapp = tk.Tk()
weatherapp.title("Weather App")
weatherapp.iconbitmap('weather_app.ico')

display_width = weatherapp.winfo_screenwidth()
display_height = weatherapp.winfo_screenheight()

left = (display_width - 900) / 2
top = (display_height - 500) / 2

weatherapp.geometry(f'900x500+{int(left)}+{int(top)}')
weatherapp.resizable(False, False)

weatherapp.mainloop()