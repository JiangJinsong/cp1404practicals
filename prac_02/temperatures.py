"""
Start
    function celsius_to_fahrenheit(celsius: real) returns real
        return (celsius * 9.0 / 5) + 32
    end function

    function fahrenheit_to_celsius(fahrenheit: real) returns real
        return (5.0 / 9) * (fahrenheit - 32)
    end function

    constant menu = "C - Convert Celsius to Fahrenheit
                     F - Convert Fahrenheit to Celsius
                     Q - Quit"

    display menu
    display "Enter choice: "
    input choice
    set choice to uppercase(choice)

    while choice ≠ "Q" do
        if choice = "C" then
            display "Enter temperature in Celsius: "
            input celsius
            set fahrenheit ← celsius_to_fahrenheit(celsius)
            display "Result: ", fahrenheit, " F"

        else if choice = "F" then
            display "Enter temperature in Fahrenheit: "
            input fahrenheit
            set celsius ← fahrenheit_to_celsius(fahrenheit)
            display "Result: ", celsius, " C"

        else
            display "Invalid option"

        display menu
        display "Enter choice: "
        input choice
        set choice to uppercase(choice)
    end while

    display "Thank you."
End
"""
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")

    print(MENU)
    choice = input(">>> ").upper()

print("Thank you.")