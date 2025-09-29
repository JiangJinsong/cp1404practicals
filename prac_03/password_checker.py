MIN_LENGTH = 8
MAX_LENGTH = 64
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|"

def is_valid(password: str) -> bool:
    if not (MIN_LENGTH <= len(password) <= MAX_LENGTH):
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for ch in password:
        if ch.islower():
            count_lower += 1
        elif ch.isupper():
            count_upper += 1
        elif ch.isdigit():
            count_digit += 1
        elif ch in SPECIAL_CHARACTERS:
            count_special += 1
    return all([count_lower, count_upper, count_digit, count_special])

def main():
    print(f"Password must be {MIN_LENGTH}-{MAX_LENGTH} chars and contain "
          f"lower, upper, digit, special ({SPECIAL_CHARACTERS}).")
    password = input("Password: ").strip()
    while not is_valid(password):
        print("Invalid password. Try again.")
        password = input("Password: ").strip()
    print(f"Your password is valid: {'*' * len(password)}")

if __name__ == "__main__":
    main()
