import tkinter as tk
from tkinter import messagebox
import emoji

def weather_forecast(temperature, wind_speed):
    if temperature > 30:
        if wind_speed < 10:
            return "🔥 Hot and Calm"
        elif 10 <= wind_speed <= 20:
            return "🌬️ Hot with Breezy Winds"
        else:
            return "💨 Hot and Windy"
    elif 20 <= temperature <= 30:
        if wind_speed < 10:
            return "😎 Moderate Temperature and Calm"
        elif 10 <= wind_speed <= 20:
            return "🍃 Moderate Temperature with Breezy Winds"
        else:
            return "🌬️ Moderate Temperature and Windy"
    else:
        return "❄️ Cool"

def convert_units(temperature, wind_speed, target_units):
    if target_units == "Fahrenheit":
        temperature = (temperature * 9/5) + 32
    return temperature, wind_speed

def get_user_input():
    temperature_input = float(entry_temp.get())
    wind_speed_input = float(entry_wind_speed.get())
    units_choice = var_units.get()
    return temperature_input, wind_speed_input, units_choice

def on_forecast_click():
    try:
        temperature_input, wind_speed_input, units_choice = get_user_input()
        forecast_result = weather_forecast(temperature_input, wind_speed_input)
        result_label.config(text=f"Weather Forecast: {forecast_result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

def on_convert_click():
    try:
        temperature_input, wind_speed_input, units_choice = get_user_input()
        temperature_input, wind_speed_input = convert_units(temperature_input, wind_speed_input, units_choice)
        result_label.config(text=f"Converted Units - Temperature: {temperature_input}°, Wind Speed: {wind_speed_input} {units_choice}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numeric values.")

def on_hover_enter(event):
    event.widget.config(bg=hover_bg_color, fg=hover_fg_color)

def on_hover_leave(event):
    event.widget.config(bg=bg_color, fg=fg_color)

root = tk.Tk()
root.title("Weather Forecasting App")

# Configure colors
bg_color = "#3498db"  # Light blue
fg_color = "#ffffff"  # White
hover_bg_color = "#2980b9"  # Slightly darker blue for hover effect
hover_fg_color = "#ecf0f1"  # Light gray for hover effect

root.configure(bg=bg_color)

# Make the GUI fullscreen
root.attributes("-fullscreen", True)

# Update font and color styles
font_style = ("Helvetica", 14, "bold")

label_temp = tk.Label(root, text="Enter the temperature (in Celsius):", bg=bg_color, fg=fg_color, font=font_style)
label_temp.pack()

entry_temp = tk.Entry(root, font=font_style)
entry_temp.pack()

label_wind_speed = tk.Label(root, text="Enter the wind speed (in km/h):", bg=bg_color, fg=fg_color, font=font_style)
label_wind_speed.pack()

entry_wind_speed = tk.Entry(root, font=font_style)
entry_wind_speed.pack()

label_units = tk.Label(root, text="Select your preferred units:", bg=bg_color, fg=fg_color, font=font_style)
label_units.pack()

var_units = tk.StringVar()
var_units.set("Celsius")

radio_celsius = tk.Radiobutton(root, text="Celsius", variable=var_units, value="Celsius", bg=bg_color, fg=fg_color, font=font_style)
radio_fahrenheit = tk.Radiobutton(root, text="Fahrenheit", variable=var_units, value="Fahrenheit", bg=bg_color, fg=fg_color, font=font_style)

radio_celsius.pack()
radio_fahrenheit.pack()

button_forecast = tk.Button(root, text="Get Weather Forecast", command=on_forecast_click, bg=bg_color, fg=fg_color, font=font_style)
button_forecast.pack(pady=10)
button_forecast.bind("<Enter>", on_hover_enter)
button_forecast.bind("<Leave>", on_hover_leave)

button_convert = tk.Button(root, text="Convert Units", command=on_convert_click, bg=bg_color, fg=fg_color, font=font_style)
button_convert.pack(pady=10)
button_convert.bind("<Enter>", on_hover_enter)
button_convert.bind("<Leave>", on_hover_leave)

result_label = tk.Label(root, text="", bg=bg_color, fg=fg_color, font=font_style)
result_label.pack(pady=20)

root.mainloop()
