import random


def determine_result(score):
    """determine the score type depend on the scores"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif 50 > score >= 0:
        return "Bad"
    elif 90 > score >= 50:
        return "Passable"
    else:
        return "Excellent"


def main():
    """determine the type of user score and determine the type of random score"""
    user_score = float(input("Enter score: "))
    print(determine_result(user_score))

    # Get a random score
    random_score = random.randint(0,100)
    print("Random score:", random_score)
    print("Result for random score:", determine_result(random_score))


main()
