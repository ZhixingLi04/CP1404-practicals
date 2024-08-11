"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""
import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # Car's odometer assertion
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Car's fuel assertion
    assert test_car.fuel == 0, "Car does not set default fuel to 0 correctly"

    test_car_with_fuel = Car(fuel=10)
    assert test_car_with_fuel.fuel == 10, "Car does not set fuel correctly when a value is provided"

    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)


def format_sentence(phrase):
    """
    Format a phrase as a sentence with a capital at the start and a period at the end.
    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("what a lovely day")
    'What a lovely day.'
    """
    return phrase.capitalize().rstrip('.') + '.'


run_tests()

# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


# (don't change the tests, change the function!)


# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass