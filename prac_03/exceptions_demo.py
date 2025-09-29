def main():
    try:
        x = int(input("Enter an integer: "))
        y = int(input("Enter another integer: "))
        print(f"{x} / {y} = {x / y}")
    except ValueError:
        print("Inputs must be integers.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    finally:
        print("Demo complete.")

if __name__ == "__main__":
    main()
