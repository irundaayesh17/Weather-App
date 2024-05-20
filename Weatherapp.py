import tkinter as tk
from tkinter import ttk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import datetime as dt

#api fetching
def getweather(city):
    try:
        API_KEY= "d1188f461e8d7b0562d962364fe01136"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        res = requests.get(url.format(city, API_KEY))
        if res:
            json = res.json()
            city = json['name']
            country = json['sys']['country']
            icon = json['weather'][0]['icon']
            temp = json['main']['temp']
            temp_celsius = temp - 273.15
            min_temp = json['main']['temp_min']
            max_temp = json['main']['temp_max']
            min_temp_celsius = min_temp - 273.15
            max_temp_celsius = max_temp - 273.15
            desc = json['weather'][0]['description']
            date = dt.datetime.now().strftime('%A, %d %B %Y %I:%M %p')

            icon_url = f"http://openweathermap.org/img/wn/{icon}.png"
            final = [city, country, date, icon_url, temp_celsius,desc , min_temp_celsius, max_temp_celsius]
            return final
        else:
            return None

    except Exception as e:
        messagebox.showerror('Error', 'An error occured, please try again.')
        print(e)


#functions
def search():
    try:
        city = search_bar.get()
        weather = getweather(city)
        if weather:
            city_name['text'] = '{}, {}'.format(weather[0], weather[1])
            date_lbl['text'] = weather[2]
            image = Image.open(requests.get(weather[3], stream=True).raw)
            icon = ImageTk.PhotoImage(image)
            weather_icon.config(image=icon)
            weather_icon.image = icon
            temp_lbl['text'] = '{:.1f}°C'.format(weather[4])
            desc_lbl['text'] = weather[5]
            maxmintemp_lbl['text'] = 'Min Temp: {:.0f}°C, Max Temp: {:.0f}°C'.format(weather[6], weather[7])
            print(weather)
        else:
            messagebox.showerror('Error', 'City not found')
    except Exception as e:
        messagebox.showerror('Error', 'An error occured.')
        print(e)

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

search_button = ttk.Button(weatherapp, text='Search', width=10, style='search.TButton', command=search)
style.configure('search.TButton', font=('Arial', 8), padding=5)
search_button.place(x=550, y=50)

city_name = ttk.Label(weatherapp, text='', style='city.TLabel')
style.configure('city.TLabel', font=('Arial', 20), foreground='white', background='blue')
city_name.place(x=370, y=100)

date_lbl = ttk.Label(weatherapp, text='', style='date.TLabel')
style.configure('date.TLabel', font=('Arial', 10), foreground='white', background='blue')
date_lbl.place(x=340, y=140)

weather_icon = ttk.Label(weatherapp, style='icon.TLabel')
style.configure('icon.TLabel', background='blue')
weather_icon.place(x=400, y=180)

temp_lbl = ttk.Label(weatherapp, text='', style='temp.TLabel')
style.configure('temp.TLabel', font=('Arial', 50, 'bold'), foreground='white', background='blue')
temp_lbl.place(x=340, y=230)

desc_lbl = ttk.Label(weatherapp, text='', style='desc.TLabel')
style.configure('desc.TLabel', font=('Arial', 15, 'bold'), foreground='white', background='blue')
desc_lbl.place(x=370, y=320)

maxmintemp_lbl = ttk.Label(weatherapp, text='', style='maxmin.TLabel')
style.configure('maxmin.TLabel', font=('Arial', 13), foreground='white', background='blue')
maxmintemp_lbl.place(x=320, y=350)

weatherapp.mainloop()