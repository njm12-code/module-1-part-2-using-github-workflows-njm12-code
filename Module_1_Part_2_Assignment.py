"""Temperature Conversion Script.

This script requests a temperature value in Fahrenheit from the user,
converts it to Celsius and Kelvin, and prints the results.
"""
def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius.

    Args:
        fahrenheit (float): Temperature in degrees Fahrenheit.

    Returns:
        float: Temperature in degrees Celsius.
    """
    return (fahrenheit - 32) * 5.0 / 9.0

