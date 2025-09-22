"""Password checker that prints stars matching password length."""

MIN_LENGTH = 8


def main():
    """Run the password check program."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length: int) -> str:
    """Get a valid password with at least min_length characters."""
    password = input("Password: ")
    while len(password) < min_length:
        print(f"Invalid. Password must be at least {min_length} characters.")
        password = input("Password: ")
    return password


def print_asterisks(password: str, symbol: str = "*") -> None:
    """Print symbols with the same length as the password."""
    print(symbol * len(password))


if __name__ == "__main__":
    main()
