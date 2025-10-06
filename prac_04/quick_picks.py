import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def generate_quick_pick():
    numbers = set()
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        numbers.add(number)
    return sorted(numbers)

def main():
    try:
        num_picks = int(input("How many quick picks? "))
        if num_picks <= 0:
            print("Please enter a positive integer.")
            return

        for _ in range(num_picks):
            quick_pick = generate_quick_pick()
            print(" ".join(f"{num:2}" for num in quick_pick))
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
