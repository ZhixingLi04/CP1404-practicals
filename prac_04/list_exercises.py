def main():
    """Main function to handle both number input and username verification."""
    get_numbers_and_print_information()
    verify_username()


def get_numbers_and_print_information():
    """Get five numbers entered by the user, store them in a list, and then output information about those numbers."""
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")


def verify_username():
    """Ask the user for their username and check if it is in the list of authorised users."""
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
        'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
        'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter your username: ")

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()

