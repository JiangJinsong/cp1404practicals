"""
Input name
Display menu
Repeat until choice is Q:
    If choice is H -> print Hello + name
    If choice is G -> print Goodbye + name
    Else -> print Invalid
"""


MENU = "(H)ello\n(G)oodbye\n(Q)uit"


def main() -> None:
    """Run the simple text menu."""
    name = input("Enter name: ").strip()
    print(MENU)
    choice = input(">>> ").strip().upper()
    while choice != "Q":
        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").strip().upper()
    print("Finished.")


if __name__ == "__main__":
    main()
