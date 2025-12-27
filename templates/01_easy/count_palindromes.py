"""
Count Palindromes

Complete the function count_palindromes(start, end) that returns how many
palindromic numbers there are between the range start and end (both inclusive).

Palindromic numbers are integers that have the same value when read from left
to right and from right to left. For example, 5, 88, 474, and 1991 are palindromes.

You can assume that start and end are always non-negative integers, and that
the value of start will always be smaller than or equal to end.

Examples:
    count_palindromes(0, 10) -> 10  (0-9 are all palindromes)
    count_palindromes(0, 100) -> 19
    count_palindromes(100, 999) -> 90
    count_palindromes(1000, 9999) -> 90
    count_palindromes(340, 450) -> 11
    count_palindromes(2002, 2002) -> 1
    count_palindromes(75, 75) -> 0
"""

# I AM NOT DONE


def count_palindromes(start, end):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_one_to_ten():
    count = count_palindromes(0, 10)
    assert count == 10


def test_one_to_hundred():
    count = count_palindromes(0, 100)
    assert count == 19


def test_three_digits():
    count = count_palindromes(100, 999)
    assert count == 90


def test_four_digits():
    count = count_palindromes(1000, 9999)
    assert count == 90


def test_arbitrary():
    count = count_palindromes(340, 450)
    assert count == 11


def test_same_start_and_end_is_palindrome():
    count = count_palindromes(2002, 2002)
    assert count == 1


def test_same_start_and_end_is_not_palindrome():
    count = count_palindromes(75, 75)
    assert count == 0


if __name__ == "__main__":
    test_one_to_ten()
    test_one_to_hundred()
    test_three_digits()
    test_four_digits()
    test_arbitrary()
    test_same_start_and_end_is_palindrome()
    test_same_start_and_end_is_not_palindrome()
    print("All tests passed!")
