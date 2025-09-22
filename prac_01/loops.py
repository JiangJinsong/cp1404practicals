"""
Print odd numbers from 1 to 20
a. Print numbers 0 to 100 step 10
b. Print numbers from 20 down to 1
c. Input count, print that many stars on one line
d. Input lines, print stars increasing from 1 to n
"""

for i in range(1, 21, 2):
    print(i, end=" ")
print()

for i in range(0, 101, 10):
    print(i, end=" ")
print()

for i in range(20, 0, -1):
    print(i, end=" ")
print()

while True:
    try:
        number_of_stars = int(input("Number of stars: "))
        break
    except ValueError:
        print("Invalid number")
print("*" * number_of_stars)

while True:
    try:
        n = int(input("Number of lines: "))
        break
    except ValueError:
        print("Invalid number")
for i in range(1, n + 1):
    print("*" * i)
