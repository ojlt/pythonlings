"""
Valid Palindrome (LeetCode #125)

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads
the same forward and backward. Alphanumeric characters include letters
and numbers.

Given a string s, return True if it is a palindrome, or False otherwise.

Examples:
    is_palindrome("A man, a plan, a canal: Panama") -> True
        # "amanaplanacanalpanama" is a palindrome
    is_palindrome("race a car") -> False
        # "raceacar" is not a palindrome
    is_palindrome(" ") -> True
        # Empty string after removing non-alphanumeric is a palindrome
"""

# I AM NOT DONE


def is_palindrome(s):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert is_palindrome("A man, a plan, a canal: Panama") == True


def test_example2():
    assert is_palindrome("race a car") == False


def test_empty():
    assert is_palindrome(" ") == True


def test_single_char():
    assert is_palindrome("a") == True


def test_numbers():
    assert is_palindrome("12321") == True


def test_mixed():
    assert is_palindrome("Was it a car or a cat I saw?") == True


def test_not_palindrome():
    assert is_palindrome("hello") == False


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_empty()
    test_single_char()
    test_numbers()
    test_mixed()
    test_not_palindrome()
    print("All tests passed!")
