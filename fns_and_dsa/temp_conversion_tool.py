import numbers
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

degree = input("Enter the temperature to convert:")
if isinstance(degree, numbers.Number) == False:
    raise TypeError("Invalid temperature. Please enter a numeric value.")
    

ForC = input("Is this temperature in Celsius or Fahrenheit? (C/F):")


def convert_to_celsius(fahrenheit):
    return ((fahrenheit-32)*FAHRENHEIT_TO_CELSIUS_FACTOR)

def convert_to_fahrenheit(celsius):
    return ((celsius*CELSIUS_TO_FAHRENHEIT_FACTOR)+32)


if ForC == 'C':
   print( degree,"°C","is",convert_to_fahrenheit(int(degree)), "°F")

if ForC == 'F':
   print( degree,"°F","is",convert_to_celsius(int(degree)), "°C")
