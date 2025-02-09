"""
Start
function determine_score_result(score)
    if score < 0 or score > 100 then
        return "Invalid score"
    else if score >= 90 then
        return "Excellent"
    else if score >= 50 then
        return "Passable"
    else
        return "Bad"
    end if
end function

function main()
    display "Enter score: "
    input score
    result ← determine_score_result(score)
    display result

    random_score ← random_integer(0, 100)
    display "Random score: ", random_score, ", Result: ", determine_score_result(random_score)
end function

call main()
End
"""
import random

def determine_score_result(score):
    """Determine the result based on the given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def main():
    """Main function to generate random scores and write results to a file."""
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}, Result: {determine_score_result(random_score)}")

if __name__ == "__main__":
    main()
