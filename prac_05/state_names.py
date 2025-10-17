"""
CP1404/CP5632 Practical
State names in a dictionary
File has been reformatted to follow PEP 8 conventions
"""

CODE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "SA": "South Australia"
}

print(CODE_TO_NAME)

# Get user input, convert to uppercase so lowercase inputs also work
state_code = input("Enter short state: ").upper()
while state_code != "":
    # EAFP approach: try to use the dictionary key directly
    try:
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

# Print all the states and names neatly lined up
for code, name in CODE_TO_NAME.items():
    print(f"{code:3} is {name}")