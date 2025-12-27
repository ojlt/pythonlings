"""
Count Vowels

Complete the function count_vowels(string) to compute how many characters
in a given string are vowels (a, e, i, o, or u). Your function should return an int.

You may assume that string will always be a str made up of lowercase letters
and/or blank spaces. This includes the empty string or a string with only
blank spaces (both of which should return 0).

Examples:
    count_vowels("lymph") -> 0
    count_vowels("python") -> 1
    count_vowels("snake") -> 2
    count_vowels("neutral") -> 3
    count_vowels("binary number") -> 4
    count_vowels("very good exam") -> 5
"""

# I AM NOT DONE


def count_vowels(string):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_zero():
    count = count_vowels("lymph")
    assert count == 0


def test_one():
    count = count_vowels("python")
    assert count == 1


def test_two():
    count = count_vowels("snake")
    assert count == 2


def test_three():
    count = count_vowels("neutral")
    assert count == 3


def test_four():
    count = count_vowels("binary number")
    assert count == 4


def test_five():
    count = count_vowels("very good exam")
    assert count == 5


if __name__ == "__main__":
    test_zero()
    test_one()
    test_two()
    test_three()
    test_four()
    test_five()
    print("All tests passed!")
