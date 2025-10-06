numbers = []

count = 1
while True:
    number = int(input(f"Number {count}: "))
    if number < 0:
        break
    numbers.append(number)
    count += 1

if numbers:
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter your username: ")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")

strings = []
unique_strings = set()
repeated_strings = set()

while True:
    user_input = input("Enter a string (or press Enter to stop): ")
    if user_input == "":
        break
    if user_input in unique_strings:
        repeated_strings.add(user_input)
    unique_strings.add(user_input)
    strings.append(user_input)

if repeated_strings:
    print("Strings repeated:", ", ".join(repeated_strings))
else:
    print("No strings were repeated.")