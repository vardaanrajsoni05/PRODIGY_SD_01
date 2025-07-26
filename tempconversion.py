def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

def main():
    print("Temperature Converter")
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit (C for Celsius, F for Fahrenheit, K for Kelvin): ").strip().upper()

    if unit == 'C':
        f = celsius_to_fahrenheit(value)
        k = celsius_to_kelvin(value)
        print(f"{value}°C = {f:.2f}°F")
        print(f"{value}°C = {k:.2f}K")
    elif unit == 'F':
        c = fahrenheit_to_celsius(value)
        k = fahrenheit_to_kelvin(value)
        print(f"{value}°F = {c:.2f}°C")
        print(f"{value}°F = {k:.2f}K")
    elif unit == 'K':
        c = kelvin_to_celsius(value)
        f = kelvin_to_fahrenheit(value)
        print(f"{value}K = {c:.2f}°C")
        print(f"{value}K = {f:.2f}°F")
    else:
        print("Invalid unit entered. Please use C, F, or K.")

if __name__ == "__main__":
    main()
