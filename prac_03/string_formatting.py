def main():
    year = 2022
    name = "Gibson L-5 CES"
    price = 16035.4
    print(f"{year} {name} for about ${price:,.2f}")
    for number in range(0, 200, 50):
        print(f"{number:>3}")
    values = [1, 19, 123, 456, -25]
    for value in values:
        print(f"Value: {value:>6}")

if __name__ == "__main__":
    main()
