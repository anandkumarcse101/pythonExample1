#16.This is the defination of the weather_forecast function and it is taking two value
#which is pass into it during the calling.
def weather_forecast(temperature, wind_speed):
    #17.Here we have use 3 condition based on the value of the temerature the below block
    #will be executed and and rturn the value.
    if temperature > 30:
        if wind_speed < 10:
            return "Hot and Calm"
        elif 10 <= wind_speed <= 20:
            return "Hot with Breezy Winds"
        else:
            return "Hot and Windy"
    elif 20 <= temperature <= 30:
        if wind_speed < 10:
            return "Moderate Temperature and Calm"
        elif 10 <= wind_speed <= 20:
            return "Moderate Temperature with Breezy Winds"
        else:
            return "Moderate Temperature and Windy"
    else:
        return "Cool"

#11.This is the defination of the get_user_input function
def get_user_input():
    #11.Here we are using while loop
    while True:
        #12.Here we are using the exception handling concept if the value enter by the 
        #User some other value insted or numeric it will handle in that case.
        try:
            #13.The below line take the input from the user as a string and perform the type casting
            #and convert it into float and finaaly store the value into temperature_input and wind_speed-input
            temperature_input = float(input("Enter the temperature (in Celsius): "))
            wind_speed_input = float(input("Enter the wind speed (in km/h): "))
        #14.This line will return the below value ie temperature_input and wind_speed_input as enter by the 
        #user
            return temperature_input, wind_speed_input
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")

#3.This is the defination of the main() function
def main():
    #4.Now the while loop will be executed until it will terminated.
    while True:
        #5.Now below 3 line will be executed on the console.
        print("\n------ Weather Forecasting App ------")
        print("1. Get Weather Forecast")
        print("2. Exit")
        #6.Now this line will be executed and expecting users input as mention below
        #7.This is imput function and it will take input as a String and as you can see
        #There is not type casting performed hence the value will be as a stings into the
        #choice variable
        choice = input("Enter your choice (1 or 2): ")
        #8.Now based on the choice value it will ececute either if block or elif block or else block
        #if the value is "1" it will execute the if block if the value is 2 it will execute the
        #elif block and if there will be other value it will execute the the esle block
        #While loop keep running until it got terminated
        if choice == "1":
            #10.The below line will call to the get_user_input() function and after getting
            #the return value from the get_user_input funtion ,It will store the value into
            #the variable temperature_input and wind-speed_input
            temperature_input, wind_speed_input = get_user_input()#Function call
            #15.As value return from the get_user_input() function and the value is stored 
            #into the above variable ie temperature_input and wind_speed_input ,here we are
            #facing these variable into the below function call which is weather_forecast.
            #Finally here we have function call and the return value stored into the forecast_result 
            forecast_result = weather_forecast(temperature_input, wind_speed_input)#Function call
            print("Weather Forecast: ",forecast_result)
        #9.when the below block executed then only while blocck will be terminated unit it will
        #keep going running.
        elif choice == "2":
            print("Exiting Weather Forecasting App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

#1.We are defining here entry point of the program
if __name__ == "__main__": 
    main()#2.Function calling


