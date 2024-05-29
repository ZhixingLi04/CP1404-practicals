"""
get sales
while sales >= 0
    calculate bonus
    Define the constant EDGE_NUMBER = 1000
    Define the constant LOW_BONUS = 0.1
    Define the constant HIGH_BONUS = 0.15
    bonus = sales * LOW_BONUS or HIGH_BONUS
    print bonus
    get sales
do next thing
"""
EDGE_NUMBER = 1000
LOW_BONUS = 0.1
HIGH_BONUS = 0.15  # data for the bonus calculation

sales = float(input("Please enter the sales: $"))

while sales >= 0:
    if sales < EDGE_NUMBER:
        bonus = sales * LOW_BONUS
    else:
        bonus = sales * HIGH_BONUS

    print(f"Bonus: ${bonus:.2f}")
    sales = float(input("Please enter the sales: $"))

print("Ended")
