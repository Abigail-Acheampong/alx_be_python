FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32.0) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32.0
    return fahrenheit

def main():
    while True:
        try:
           temp_input = input("Enter the temperature to convert: ")
           temperature = float(temp_input)

           while True:
               choice = input("Is thos temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
               if choice in ("C", "F"):
                   break
               else:
                   print("Invlaid choice. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

           if choice == "C":
              temp_in_fahrenheit = convert_to_fahrenheit(temperature)
              print(f"{temperature}֯ C is {temp_in_fahrenheit}֯ F")

           elif choice == "F":
              temp_in_celsius = convert_to_celsius(temperature)
              print(f"{temperature}֯ F is {temp_in_celsius}֯ C") 
           break

        except ValueError:
            print("Invlaid temperature. Please enter a numeric value.")       

if __name__ == "__main__":
    main()