import random

# Line 1: Generates a random integer between 5 and 20, inclusive.
print(random.randint(5, 20))  # Example output: 12
# The smallest number possible: 5
# The largest number possible: 20

# Line 2: Generates a random number from the range 3 to 9 with a step of 2 (i.e., 3, 5, 7, 9)
print(random.randrange(3, 10, 2))  # Example output: 7
# The smallest number possible: 3
# The largest number possible: 9
# Could this line have produced a 4? No, because the step is 2, meaning only 3, 5, 7, or 9 can be selected.

# Line 3: Generates a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # Example output: 4.23
# The smallest number possible: 2.5
# The largest number possible: 5.5

# Code to generate a random number between 1 and 100 inclusive
print(random.randint(1, 100))
