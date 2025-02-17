name = input("Enter your name: ")
file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
name = file.read().strip()
file.close()
print(f"Hi {name}!")

with open("numbers.txt", "r") as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
    total = num1 + num2
print(total)

with open("numbers.txt", "r") as file:
    total = sum(int(line.strip()) for line in file)  # Sum all numbers
print(total)