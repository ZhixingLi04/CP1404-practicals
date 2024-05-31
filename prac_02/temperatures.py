Menu =("C - Convert Celsius to Fahrenheit\n"
       "F - Convert Fahrenheit to Celsius\n"
       "Q - Quit\n")


def celsius_to_fahrenheit(celsius):
    """calculate the value of celsius"""
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """calculate the value of fahrenheit"""
    return 5 / 9 * (fahrenheit - 32)


def main():
    """convert celsius to fahrenheit and celsius to fahrenheit"""
    print(Menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            result = celsius_to_fahrenheit(celsius)
            print(f"Result: {result:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {result:.2f} C")
        else:
            print("Invalid option")
        print(Menu)
        choice = input(">>> ").upper()
    print("Thank you.")

main()