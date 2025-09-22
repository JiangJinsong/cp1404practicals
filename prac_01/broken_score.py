"""
Input score
If score < 0 or > 100 -> print Invalid
Else if score >= 90 -> print Excellent
Else if score >= 50 -> print Passable
Else -> print Bad
"""


from typing import Final

MIN_SCORE: Final = 0
MAX_SCORE: Final = 100
EXCELLENT_THRESHOLD: Final = 90
PASSABLE_THRESHOLD: Final = 50


def classify(score: float) -> str:
    """Return the textual classification for a given score."""
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    if score >= PASSABLE_THRESHOLD:
        return "Passable"
    return "Bad"


def main() -> None:
    """Prompt for a score and print the classification."""
    try:
        score = float(input("Score: "))
    except ValueError:
        print("Invalid number")
    else:
        print(classify(score))


if __name__ == "__main__":
    main()
