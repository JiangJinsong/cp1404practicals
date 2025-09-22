"""
Display menu
Get user choice
If choice is C -> input Celsius, convert to Fahrenheit, print result
If choice is F -> input Fahrenheit, convert to Celsius, print result
Else -> print invalid
Repeat until choice is Q
"""


MENU = "(C)elsius to Fahrenheit\n(F)ahrenheit to Celsius\n(Q)uit"


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main() -> None:
    """Run the menu-driven temperature conversion program."""
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "C":
            try:
                celsius = float(input("Celsius: "))
            except ValueError:
                print("Invalid number")
            else:
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            try:
                fahrenheit = float(input("Fahrenheit: "))
            except ValueError:
                print("Invalid number")
            else:
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Finished.")


if __name__ == "__main__":
    main()
