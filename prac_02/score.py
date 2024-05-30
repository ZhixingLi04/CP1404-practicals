

score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif 50 > score >= 0:
    print("Bad")
elif 90 > score >= 50:
    print("Passable")
else:
    print("Excellent")
