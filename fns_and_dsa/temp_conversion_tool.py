fahrenheit_to_celsius_factor = 5/9
celsius_to_fahrenheit_factor = 9/5

def convert_to_celsius():
    converted_temp = (temperature - 32) * fahrenheit_to_celsius_factor
    print(temperature,"°F is", converted_temp, "°C")

def convert_to_fahrenheit():
    converted_temp =  (temperature * celsius_to_fahrenheit_factor) + 32
    print(temperature, "°C is", converted_temp, "°F")


temperature = (input("Enter the temperature to convert: "))
factor = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

if factor == "f" and temperature.isnumeric():
    convert_to_celsius()
elif factor == "c" and temperature.isnumeric():
    convert_to_fahrenheit()
else:
    print("Invalid temperature. Please enter a numeric value.")