"""
Start
define main()
    get name
    choice = ""
    while choice != "Q"
        display menu
        get choice
        choice = choice converted to uppercase
        if choice == "H"
            display "Hello" name
        else if choice == "G"
            display "Goodbye" name
        else if choice == "Q"
            display "Finished."
        else
            display "Invalid choice"
End
"""
def main():
    name = input("Enter name: ")
    choice = ""
    while choice != "Q":
        print("\n(H)ello")
        print("(G)oodbye")
        print("(Q)uit")
        choice = input(">>> ").upper()

        if choice == "H":
            print(f"Hello {name}")
        elif choice == "G":
            print(f"Goodbye {name}")
        elif choice == "Q":
            print("Finished.")
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()