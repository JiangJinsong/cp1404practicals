"""Score categoriser with deterministic and random evaluation."""
from random import randint


def main():
    """Ask for a score, print its category, then do a random example."""
    try:
        score = float(input("Score: "))
    except ValueError:
        print("Invalid input")
    else:
        print(evaluate_score(score))
    random_score = float(randint(0, 100))
    print(f"Random score: {random_score:.0f} -> {evaluate_score(random_score)}")


def evaluate_score(score: float) -> str:
    """Return the category string for a score in [0, 100]."""
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    if score >= 50:
        return "Passable"
    return "Bad"


if __name__ == "__main__":
    main()
