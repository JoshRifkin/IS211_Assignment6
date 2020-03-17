# Assignment 6
# By: Joshua Rifkin

import unittest
import conversions
import conversions_refactored


class ConvertCelsiusTest(unittest.TestCase):

    def testToFahrenheit(self):
        knownVals = ((300, 572), (0, 32), (26, 78.8), (-53, -63.4), (124, 255.2), (-1, 30.2))
        for cel, far in knownVals:
            result = conversions.convertCelsiusToFahrenheit(cel)
            self.assertAlmostEqual(result, far)

    def testToKelvin(self):
        knownVals = ((300, 573.15), (0, 273.15), (26, 299.15), (-53, 220.15), (124, 397.15), (-1, 272.15))
        for cel, kel in knownVals:
            result = conversions.convertCelsiusToKelvin(cel)
            self.assertAlmostEqual(result, kel)


class ConvertFahrenheitTest(unittest.TestCase):

    def testToCelsius(self):
        knownVals = ((300, 572), (0, 32), (26, 78.8), (-53, -63.4), (124, 255.2), (-1, 30.2))
        for cel, far in knownVals:
            result = conversions.convertFahrenheitToCelsius(far)
            self.assertAlmostEqual(result, cel)

    def testToKelvin(self):
        knownVals = ((572, 573.15), (32, 273.15), (78.8, 299.15), (-63.4, 220.15), (255.2, 397.15), (30.2, 272.15))
        for far, kel in knownVals:
            result = conversions.convertFahrenheitToKelvin(far)
            self.assertAlmostEqual(result, kel)


class ConvertKelvinTest(unittest.TestCase):

    def testToCelsius(self):
        knownVals = ((300, 573.15), (0, 273.15), (26, 299.15), (-53, 220.15), (124, 397.15), (-1, 272.15))
        for cel, kel in knownVals:
            result = conversions.convertKelvinToCelsius(kel)
            self.assertAlmostEqual(result, cel)

    def testToFahrenheit(self):
        knownVals = ((572, 573.15), (32, 273.15), (78.8, 299.15), (-63.4, 220.15), (255.2, 397.15), (30.2, 272.15))
        for far, kel in knownVals:
            result = conversions.convertKelvinToFahrenheit(kel)
            self.assertAlmostEqual(result, far)


class testRefactored(unittest.TestCase):

    def testKnownConversions(self):

        knownConversions = (
            ("Fahrenheit", "Celsius", 32, 0),
            ("Fahrenheit", "Kelvin", 32, 273.15),
            ("Celsius", "Fahrenheit", 0, 32),
            ("Celsius", "Kelvin", 0, 273.15),
            ("Kelvin", "Fahrenheit", 273.15, 32),
            ("Kelvin", "Celsius", 273.15, 0),
            ("Miles", "Yards", 10.0000032, 17600.005632),
            ("Miles", "Meters", 10.000003199999499159, 16093.477339910294),
            ("Yards", "Miles", 1000.00032, 0.568182),
            ("Yards", "Meters", 1000.00032, 914.400292608),
            ("Meters", "Miles", 999.99698399997066645, 0.621368075325186),
            ("Meters", "Yards", 999.996984, 1093.61)
        )

        for (fromUnit, toUnit, fromVal, toVal) in knownConversions:
            result = conversions_refactored.convert(fromUnit, toUnit, fromVal)
            self.assertAlmostEqual(result, toVal)

    def testSameConversions(self):
        sameConversions = (
            ("fahrenheit", "fahrenheit", 1245, 1245),
            ("celsius", "celsius", 1245, 1245),
            ("kelvin", "kelvin", 1245, 1245),
            ("miles", "miles", 1245, 1245),
            ("yards", "yards", 1245, 1245),
            ("meters", "meters", 1245, 1245),
        )
        for (fromUnit, toUnit, fromVal, toVal) in sameConversions:
            result = conversions_refactored.convert(fromUnit, toUnit, fromVal)
            self.assertAlmostEqual(result, toVal)

    def testBadConversions(self):
        badConversions = (
            ("Fahrenheit", "Meter", 123, 123),
            ("Celsius", "Mile", 123, 123),
            ("Mile", "Kelvin", 123, 123),
            ("Yard", "Fahrenheit", 123, 123)
        )
        for (fromUnit, toUnit, fromVal, toVal) in badConversions:
            self.assertRaises(conversions_refactored.ConversionNotPossible,
                              conversions_refactored.convert(fromUnit, toUnit, fromVal))


if __name__ == '__main__':
    unittest.main()