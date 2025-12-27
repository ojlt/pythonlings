"""
Valid Parentheses (LeetCode #20)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Examples:
    is_valid("()") -> True
    is_valid("()[]{}") -> True
    is_valid("(]") -> False
    is_valid("([)]") -> False
    is_valid("{[]}") -> True
"""

# I AM NOT DONE


def is_valid(s):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_simple_valid():
    assert is_valid("()") == True


def test_multiple_valid():
    assert is_valid("()[]{}") == True


def test_wrong_type():
    assert is_valid("(]") == False


def test_wrong_order():
    assert is_valid("([)]") == False


def test_nested_valid():
    assert is_valid("{[]}") == True


def test_empty():
    assert is_valid("") == True


def test_single_open():
    assert is_valid("(") == False


def test_single_close():
    assert is_valid(")") == False


def test_complex_valid():
    assert is_valid("({[]})") == True


if __name__ == "__main__":
    test_simple_valid()
    test_multiple_valid()
    test_wrong_type()
    test_wrong_order()
    test_nested_valid()
    test_empty()
    test_single_open()
    test_single_close()
    test_complex_valid()
    print("All tests passed!")
