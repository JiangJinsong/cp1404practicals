"""
Loop:
    Input sales
    If sales < 0 -> exit loop
    If sales >= 1000 -> bonus = sales * 15%
    Else -> bonus = sales * 10%
    Print bonus
End loop
"""


def compute_bonus(sales: float) -> float:
    """Return the bonus based on tiered rates."""
    rate = 0.15 if sales >= 1000 else 0.10
    return sales * rate


def main() -> None:
    """Prompt for sales amounts until a negative value is entered."""
    while True:
        try:
            sales = float(input("Enter sales: $"))
        except ValueError:
            print("Invalid number")
            continue
        if sales < 0:
            break
        bonus = compute_bonus(sales)
        print(f"Bonus: ${bonus:.2f}")
    print("Finished.")


if __name__ == "__main__":
    main()