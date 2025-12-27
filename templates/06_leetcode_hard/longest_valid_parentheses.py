"""
Longest Valid Parentheses (LeetCode #32)

Given a string containing just the characters '(' and ')', return the length
of the longest valid (well-formed) parentheses substring.

Examples:
    longest_valid_parentheses("(()") -> 2
        # The longest valid parentheses substring is "()"
    longest_valid_parentheses(")()())") -> 4
        # The longest valid parentheses substring is "()()"
    longest_valid_parentheses("") -> 0
"""

# I AM NOT DONE


def longest_valid_parentheses(s):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert longest_valid_parentheses("(()") == 2


def test_example2():
    assert longest_valid_parentheses(")()())") == 4


def test_empty():
    assert longest_valid_parentheses("") == 0


def test_all_open():
    assert longest_valid_parentheses("((((") == 0


def test_all_close():
    assert longest_valid_parentheses("))))") == 0


def test_perfect():
    assert longest_valid_parentheses("()()()") == 6


def test_nested():
    assert longest_valid_parentheses("((()))") == 6


def test_complex():
    assert longest_valid_parentheses("()(()") == 2


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_empty()
    test_all_open()
    test_all_close()
    test_perfect()
    test_nested()
    test_complex()
    print("All tests passed!")
