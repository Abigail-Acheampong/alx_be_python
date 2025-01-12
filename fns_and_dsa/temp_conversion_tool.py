FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32.0) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32.0

def main():
    try:
        # Get temperature input
        temp_input = input("Enter the temperature to convert: ")
        try:
            temperature = float(temp_input)
        except ValueError:
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        # Get unit input
        unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit_input not in ("C", "F"):
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

        # Perform conversion
        if unit_input == "C":
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature:.2f}\u00b0C is {converted_temp:.2f}\u00b0F")
        elif unit_input == "F":
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature:.2f}\u00b0F is {converted_temp:.2f}\u00b0C")

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
