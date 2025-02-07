"""
Start
define get_valid_number(prompt)
    while True
        try
            number = input(prompt) as integer
            if number < 0
                print "Invalid number of items!"
            else
                return number
        catch ValueError
            print "Please enter a valid integer."

define get_valid_price(prompt)
    while True
        try
            price = input(prompt) as float
            if price < 0
                print "Price must be >= $0"
            else
                return price
        catch ValueError
            print "Please enter a valid number."

define main()
    num_items = get_valid_number("Number of items: ")
    total_price = 0

    for i from 1 to num_items
        price = get_valid_price("Price of item: ")
        total_price += price

    if total_price > 100
        total_price *= 0.9  # Apply 10% discount

    print f"Total price for {num_items} items is ${total_price:.2f}"

if __name__ == "__main__"
    main()
End
"""
"""
Program to calculate the total price for a number of items with different prices.
If the total price is over $100, a 10% discount is applied.
"""
def get_valid_number(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number < 0:
                print("Invalid number of items!")
            else:
                return number
        except ValueError:
            print("Please enter a valid integer.")

def get_valid_price(prompt):
    while True:
        try:
            price = float(input(prompt))
            if price < 0:
                print("Price must be >= $0")
            else:
                return price
        except ValueError:
            print("Please enter a valid number.")

def main():
    num_items = get_valid_number("Number of items: ")
    total_price = 0

    for _ in range(num_items):
        price = get_valid_price("Price of item: ")
        total_price += price

    if total_price > 100:
        total_price *= 0.9  # Apply 10% discount

    print(f"Total price for {num_items} items is ${total_price:.2f}")

if __name__ == "__main__":
    main()
