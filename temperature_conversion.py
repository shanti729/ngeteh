def convert_celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin"""
    kelvin = celsius + 273.15
    return kelvin

def convert_kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius"""
    celsius = kelvin - 273.15
    return celsius

def convert_fahrenheit_to_kelvin(fahrenheit):
    """Convert Fahrenheit to Kelvin"""
    celsius = convert_fahrenheit_to_celsius(fahrenheit)
    kelvin = convert_celsius_to_kelvin(celsius)
    return kelvin

def convert_kelvin_to_fahrenheit(kelvin):
    """Convert Kelvin to Fahrenheit"""
    celsius = convert_kelvin_to_celsius(kelvin)
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    return fahrenheit