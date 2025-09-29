def read_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid integer. Try again.")

def main():
    numerator = read_int("Enter the numerator: ")
    denominator = read_int("Enter the denominator (non-zero): ")
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = read_int("Enter the denominator (non-zero): ")
    fraction = numerator / denominator
    print(f"Result: {fraction}")
    print("Finished.")

if __name__ == "__main__":
    main()
