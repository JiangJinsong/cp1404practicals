"""Temperature converter using SRP-compliant functions."""

def main():
    """Menu to convert temperatures between Celsius and Fahrenheit."""
    MENU = "(C)elsius to Fahrenheit  (F)ahrenheit to Celsius  (Q)uit"
    print(MENU)
    choice = input("Choice: ").strip().upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_float("Celsius: ")
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = get_float("Fahrenheit: ")
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("Choice: ").strip().upper()
    print("Done")


def get_float(prompt: str) -> float:
    """Get a valid float from user input."""
    value = None
    while value is None:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Invalid number")
    return value


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    main()