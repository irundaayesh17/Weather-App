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
weatherapp.configure(bg='blue')

style = ttk.Style()

search_bar = ttk.Entry(weatherapp, width=40, style='search.TEntry')
style.configure('search.TEntry', font=('Arial', 15))
search_bar.place(x=300, y=50)

search_button = ttk.Button(weatherapp, text='Search', width=10, style='search.TButton')
style.configure('search.TButton', font=('Arial', 8), padding=5)
search_button.place(x=550, y=50)

city_name = ttk.Label(weatherapp, text='', style='city.TLabel')
style.configure('city.TLabel', font=('Arial', 20), foreground='white', background='blue')
city_name.place(x=370, y=100)

date_lbl = ttk.Label(weatherapp, text='', style='date.TLabel')
style.configure('date.TLabel', font=('Arial', 10), foreground='white', background='blue')
date_lbl.place(x=400, y=140)

weather_icon = ttk.Label(weatherapp, style='icon.TLabel')
style.configure('icon.TLabel', background='blue')
weather_icon.place(x=400, y=200)

temp_lbl = ttk.Label(weatherapp, text='', style='temp.TLabel')
style.configure('temp.TLabel', font=('Arial', 35, 'bold'), foreground='white', background='blue')
temp_lbl.place(x=400, y=250)

desc_lbl = ttk.Label(weatherapp, text='', style='desc.TLabel')
style.configure('desc.TLabel', font=('Arial', 15, 'bold'), foreground='white', background='blue')
desc_lbl.place(x=400, y=310)

maxmintemp_lbl = ttk.Label(weatherapp, text='', style='maxmin.TLabel')
style.configure('maxmin.TLabel', font=('Arial', 13), foreground='white', background='blue')
maxmintemp_lbl.place(x=400, y=350)

weatherapp.mainloop()