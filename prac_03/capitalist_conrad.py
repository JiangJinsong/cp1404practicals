import random

START_PRICE = 10.0
MIN_CHANGE = -0.10
MAX_CHANGE = 0.10
MAX_DAYS = 365
MIN_PRICE = 1.0
MAX_PRICE = 1000.0
OUTPUT_FILE = "price_simulation.txt"

def main():
    price = START_PRICE
    lines = [f"Starting price: ${price:,.2f}"]
    for day in range(1, MAX_DAYS + 1):
        change = random.uniform(MIN_CHANGE, MAX_CHANGE)
        price *= (1 + change)
        lines.append(f"On day {day} price is: ${price:,.2f}")
        if price <= MIN_PRICE or price >= MAX_PRICE:
            break
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
        out_file.write("\n".join(lines))

if __name__ == "__main__":
    main()
