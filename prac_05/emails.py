def main():
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        default_name = get_name_from_email(email)

        confirmation = input(f"Is your name {default_name}? (Y/n) ").lower()
        if confirmation not in ("", "y"):
            # If user types anything other than just Enter or 'y', ask for their name
            default_name = input("Name: ")

        email_to_name[email] = default_name

        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")

def get_name_from_email(email):
    username = email.split("@")[0]
    parts = username.split(".")
    return " ".join(parts).title()

if __name__ == "__main__":
    main()