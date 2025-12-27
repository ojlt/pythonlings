"""
Roman to Integer

Complete the function roman_to_int(numeral) that converts a Roman numeral
string numeral from a str to an integer.

You can assume the input is always a valid Roman numeral in the range [1, 3999].
The Roman numerals are:
    I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

Subtractive rules apply:
- I can be placed before V (5) and X (10) to make 4 and 9.
- X can be placed before L (50) and C (100) to make 40 and 90.
- C can be placed before D (500) and M (1000) to make 400 and 900.

Examples:
    roman_to_int("III") -> 3
    roman_to_int("LVIII") -> 58
    roman_to_int("MCMXCIV") -> 1994
    roman_to_int("IX") -> 9
    roman_to_int("CDXLIV") -> 444
"""

# I AM NOT DONE


def roman_to_int(numeral):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_three():
    assert roman_to_int("III") == 3


def test_fifty_eight():
    assert roman_to_int("LVIII") == 58


def test_1994():
    assert roman_to_int("MCMXCIV") == 1994


def test_nine():
    assert roman_to_int("IX") == 9


def test_444():
    assert roman_to_int("CDXLIV") == 444


if __name__ == "__main__":
    test_three()
    test_fifty_eight()
    test_1994()
    test_nine()
    test_444()
    print("All tests passed!")
