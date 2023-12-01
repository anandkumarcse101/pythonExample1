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

def get_user_input():
    while True:
        try:
            temperature_input = float(input("Enter the temperature (in Celsius): "))
            wind_speed_input = float(input("Enter the wind speed (in km/h): "))
            return temperature_input, wind_speed_input
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

def main():
    while True:
        print("\n------ Weather Forecasting App ------")
        print("1. Get Weather Forecast")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            temperature_input, wind_speed_input = get_user_input()
            forecast_result = weather_forecast(temperature_input, wind_speed_input)
            print(f"Weather Forecast: {forecast_result}")
        elif choice == "2":
            print("Exiting Weather Forecasting App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
