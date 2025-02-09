"""
Start
function print_grid(number_of_rows, number_of_columns)
    for i <- 1 to number_of_rows do
        print "*" repeated number_of_columns times
    end for
end function

function get_valid_score()
    repeat
        display "Enter a valid score (0-100): "
        input score
        if score >= 0 and score <= 100 then
            return score
        else
            display "Invalid score! Please enter a number between 0 and 100."
        endif
    until score is valid
end function

function determine_grade(score)
    if score >= 85 then
        return "High Distinction"
    elseif score >= 75 then
        return "Distinction"
    elseif score >= 65 then
        return "Credit"
    elseif score >= 50 then
        return "Pass"
    else
        return "Fail"
    endif
end function

function show_stars(score)
    for i <- 1 to score do
        print "*"
    end for
end function

procedure main()
    display "Welcome to the score program!"
    set score <- get_valid_score()

    repeat
        display "\nMenu:"
        display "(G)et a valid score"
        display "(P)rint result"
        display "(S)how stars"
        display "(Q)uit"
        display "Choose an option: "
        input choice
        set choice <- to_lower(choice)

        if choice = "g" then
            set score <- get_valid_score()
        elseif choice = "p" then
            display "Your grade is: " + determine_grade(score)
        elseif choice = "s" then
            show_stars(score)
        elseif choice = "q" then
            display "Goodbye! Thanks for using the program."
        else
            display "Invalid choice. Please try again."
        endif
    until choice = "q"

call main()
End
"""
def print_grid(number_of_rows, number_of_columns):
    """Print a grid of stars with the specified rows and columns."""
    for _ in range(number_of_rows):
        print('*' * number_of_columns)

def get_valid_score():
    """Get a valid score between 0 and 100 inclusive."""
    while True:
        try:
            score = int(input("Enter a valid score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score! Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

def determine_grade(score):
    """Determine the grade based on the score."""
    if score >= 85:
        return "High Distinction"
    elif score >= 75:
        return "Distinction"
    elif score >= 65:
        return "Credit"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"

def show_stars(score):
    """Print as many stars as the score."""
    print('*' * score)

def main():
    """Main function to handle the menu-driven program."""
    print("Welcome to the score program!")
    score = get_valid_score()

    while True:
        print("\nMenu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Choose an option: ").strip().lower()

        if choice == 'g':
            score = get_valid_score()
        elif choice == 'p':
            print(f"Your grade is: {determine_grade(score)}")
        elif choice == 's':
            show_stars(score)
        elif choice == 'q':
            print("Goodbye! Thanks for using the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()