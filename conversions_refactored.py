# Assignment 6
# By: Joshua Rifkin


class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    conversions = {
        ("fahrenheit", "celsius"): "(value - 32) * (5/9)",
        ("fahrenheit", "kelvin"): "(value + 459.67) * (5/9)",
        ("celsius", "fahrenheit"): "(value * (9/5)) + 32",
        ("celsius", "kelvin"): "value + 273.15",
        ("kelvin", "celsius"): "value - 273.15",
        ("kelvin", "fahrenheit"): "(value * (9/5)) - 459.67",
        ("miles", "yards"): "value * 1760",
        ("miles", "meters"): "value * 1609.347219",
        ("yards", "miles"): "value / 1760",
        ("yards", "meters"): "value * .9144",
        ("meters", "miles"): "value / 1609.347219",
        ("meters", "yards"): "value / .9144",
    }

    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()

    if fromUnit == toUnit:
        return float(value)
    elif (fromUnit, toUnit) in conversions.keys():
        converted = eval(conversions[(fromUnit, toUnit)])
        return float(converted)
    else:
        raise ConversionNotPossible("These two data types are not compatible.")
