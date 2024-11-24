import requests
import tkinter as tk
from tkinter import messagebox

# Function to fetch weather data
def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    api_key = "replace with you APIkey"  # Replace with your API key
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        weather_data = response.json()

        # Extracting relevant data
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        # Display the weather information
        weather_info.set(f"Weather in {city.title()}:\n"
                         f"Temperature: {temp}°C\n"
                         f"Humidity: {humidity}%\n"
                         f"Description: {description.capitalize()}")
    except requests.exceptions.RequestException:
        messagebox.showerror("Error", "Unable to fetch data. Check your internet or city name.")
    except KeyError:
        messagebox.showerror("Error", "Invalid city name or API response.")

# Setting up the GUI
app = tk.Tk()
app.title("Weather App")

# City input
city_label = tk.Label(app, text="Enter City:", font=("Arial", 14))
city_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")  # Positioned at row 0, column 0

city_entry = tk.Entry(app, font=("Arial", 14))
city_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # Positioned at row 0, column 1

# Get Weather Button
fetch_button = tk.Button(app, text="Get Weather", command=get_weather, font=("Arial", 14))
fetch_button.grid(row=1, column=0, columnspan=2, pady=10)

# Weather display
weather_info = tk.StringVar()
weather_label = tk.Label(app, textvariable=weather_info, font=("Arial", 12), justify="left")
weather_label.grid(row=2, column=0, columnspan=2, padx=10, pady=20)

# Ensure app resizes
app.resizable(True, True)

# Force update
app.update()

# Run the app
app.mainloop()
