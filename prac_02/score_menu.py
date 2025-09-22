"""Menu-driven score utility using SRP and reusable functions."""
from typing import Union
from score import evaluate_score  # reuse per prac requirement


def main():
    """Provide a menu for score operations."""
    score = get_valid_score()
    while True:
        print("(G)et a valid score  (P)rint result  (S)how stars  (Q)uit")
        choice = input("Choice: ").strip().upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(evaluate_score(score))
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Farewell")
            break
        else:
            print("Invalid choice")


def get_valid_score() -> float:
    """Get a valid score in 0..100 inclusive."""
    score: Union[int, float, None] = None
    while score is None:
        try:
            candidate = float(input("Score (0-100): "))
        except ValueError:
            print("Invalid input")
            continue
        if 0 <= candidate <= 100:
            score = candidate
        else:
            print("Score must be between 0 and 100 inclusive")
    return float(score)


def show_stars(score: Union[int, float]) -> None:
    """Print stars equal to the integer part of score."""
    print("*" * int(score))


if __name__ == "__main__":
    main()