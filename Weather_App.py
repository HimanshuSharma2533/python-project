# pip install requests

import tkinter as tk
import requests

# Replace with your actual OpenWeatherMap API key
API_KEY = "your_api_key_here"

def get_weather():
    city = city_entry.get()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            weather = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            result = (
                f"Weather in {city}:\n"
                f"Temperature: {temp}°C\n"
                f"Condition: {weather}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind} m/s"
            )
        else:
            result = f"City not found: {city}"
    except Exception as e:
        result = f"Error: {e}"

    result_label.config(text=result)

# GUI setup
root = tk.Tk()
root.title("Weather App")
root.geometry("300x300")

tk.Label(root, text="Enter City Name:").pack(pady=10)
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack(pady=10)

root.mainloop()