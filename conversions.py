# Assignment 6
# By: Joshua Rifkin



def convertCelsiusToKelvin(celsius):
    kelvin = celsius + 273.15
    return float(kelvin)


def convertCelsiusToFahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return float(fahrenheit)


def convertFahrenheitToCelsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return float(celsius)


def convertFahrenheitToKelvin(fahrenheit):
    kelvin = (fahrenheit + 459.67) * (5/9)
    return float(kelvin)


def convertKelvinToCelsius(kelvin):
    celsius = (kelvin - 273.15)
    return float(celsius)


def convertKelvinToFahrenheit(kelvin):
    fahrenheit = (kelvin * (9/5)) - 459.67
    return float(fahrenheit)

