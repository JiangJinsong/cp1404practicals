"""
Start
get sales
while sales >= 0
    if sales < 1000
        bonus = sales * 0.10
    else
        bonus = sales * 0.15
    print bonus
    get sales
End
"""
sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.10
    else:
        bonus = sales * 0.15
    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))