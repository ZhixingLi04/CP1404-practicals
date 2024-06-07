"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer：A ValueError will occur if I input a non-integer value for either the numerator or the denominator.
2. When will a ZeroDivisionError occur?
Answer：A ZeroDivisionError will occur if I input 0 as the value for the denominator,
resulting in division by zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Answer： we can change the code to avoid the possibility of a ZeroDivisionError by checking if the denominator is zero
before performing the division operation.
If the denominator is zero, I can handle it separately by printing an appropriate error message.
"""
initial = False
while not initial:
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        while denominator == 0:
            print("denominator can not equal to 0")
            denominator = int(input("Enter the numerator:"))
        fraction = numerator / denominator
        print(fraction)
        initial = True
    except ValueError:
        print("Numerator and denominator must be valid numbers!")

    except ZeroDivisionError:
        print("Cannot divide by Zero!")
print("Finished.")
