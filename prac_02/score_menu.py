def get_valid_score():
    """get the valid score"""
    score = float(input("Enter a valid score (0-100): "))
    while score == "" or score <= 0 or score > 100:
          print("Invalid score! Please enter a score between 0 and 100.")
          score = float(input("Enter a valid score (0-100): "))
    return score


def determine_result(score):
    """determine the types of score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif 50 > score >= 0:
        return "Bad"
    elif 90 > score >= 50:
        return "Passable"
    else:
        return "Excellent"




def print_result(score):
    """show the result"""
    result = determine_result(score)
    print(f"The result for the score {score} is: {result}")


def show_stars(score):
    """show the stars depend on the scores"""
    print("*" * int(score))


def main():
    """Select different functions in the menu"""
    choice = ""
    score = ""
    while choice != "Q":
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")
        choice = input("Enter your choice: ").strip().upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score == "":
                print("error massage")
            else:
                print_result(score)
        elif choice == "S":
            if score == "":
                print("error massage")
            else:
                show_stars(score)
        elif choice == "Q":
            print("Thank you!")
        else:
            print("Invalid choice. Please select a valid option.")



main()
