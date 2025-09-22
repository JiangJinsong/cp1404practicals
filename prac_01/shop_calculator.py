"""
Input number of items (must be >= 0)
For each item:
    Input price (must be >= 0)
    Add to total
If total > 100 -> apply 10% discount
Print total
"""


from typing import Final

DISCOUNT_THRESHOLD: Final = 100.0
DISCOUNT_RATE: Final = 0.10


def main() -> None:
    """Calculate total price with optional discount."""
    while True:
        try:
            number_of_items = int(input("Number of items: "))
        except ValueError:
            print("Invalid number of items!")
            continue
        if number_of_items < 0:
            print("Invalid number of items!")
            continue
        break

    total = 0.0
    for _ in range(number_of_items):
        while True:
            try:
                price = float(input("Price of item: "))
            except ValueError:
                print("Invalid price")
                continue
            if price < 0:
                print("Invalid price")
                continue
            break
        total += price

    if total > DISCOUNT_THRESHOLD:
        total *= 1 - DISCOUNT_RATE

    print(f"Total price for {number_of_items} items is ${total:.2f}")


if __name__ == "__main__":
    main()
