"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.

    >>> repeat_string("hi", 2)
    'hi hi'
    >>> repeat_string("Python", 1)
    'Python'
    """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital letter and ending with a single full stop.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("this is a test")
    'This is a test.'
    """
    phrase = phrase.strip()
    if not phrase:
        return ""
    # Capitalize the first letter.
    phrase = phrase[0].upper() + phrase[1:]
    # Remove any trailing full stops and add a single one.
    phrase = phrase.rstrip(".")
    return phrase + "."


def run_tests():
    """Run the tests on the functions."""
    # Test for repeat_string
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # Test that Car's __init__ sets the odometer correctly.
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # Test that Car sets the fuel correctly.
    default_car = Car()
    assert default_car.fuel == 0, "Default fuel should be 0"
    car_with_fuel = Car(fuel=10)
    assert car_with_fuel.fuel == 10, "Fuel should be set to 10 when provided"


if __name__ == '__main__':
    run_tests()
    doctest.testmod()