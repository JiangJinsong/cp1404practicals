updated_code_with_answers ="""
CP1404/CP5632 - Practical
Answer the following questions:

1. When will a ValueError occur?
   - A ValueError will occur when the user inputs a non-integer value for either the numerator or denominator.
   - This happens if the user enters text (e.g., "abc") or a decimal number (e.g., "3.5").
   - The int() function in Python cannot convert non-integer values, leading to this error.

2. When will a ZeroDivisionError occur?
   - A ZeroDivisionError will occur when the user enters 0 as the denominator.
   - Division by zero is mathematically undefined and is not allowed in Python.
   - This causes Python to raise a ZeroDivisionError.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
   - Yes, we can modify the code to repeatedly prompt the user until they enter a non-zero denominator.
   - Instead of allowing the user to enter 0 and then handling the error, we can use a loop:
       - Keep asking for the denominator until the user enters a valid, non-zero number.
       - This prevents a ZeroDivisionError from ever occurring.
"""
try:
    numerator = int(input("Enter the numerator: "))
    denominator = 0
    while denominator == 0:  # Ensure denominator is not zero
        denominator = int(input("Enter the denominator (must not be 0): "))
        if denominator == 0:
            print("Denominator cannot be zero. Please enter a non-zero number.")

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

with open("file_path", "w") as file:
    file.write(updated_code_with_answers)