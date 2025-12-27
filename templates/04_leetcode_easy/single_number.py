"""
Single Number (LeetCode #136)

Given a non-empty array of integers nums, every element appears twice
except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use
only constant extra space.

Examples:
    single_number([2, 2, 1]) -> 1
    single_number([4, 1, 2, 1, 2]) -> 4
    single_number([1]) -> 1

Hint: Think about the XOR operation and its properties.
"""

# I AM NOT DONE


def single_number(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert single_number([2, 2, 1]) == 1


def test_example2():
    assert single_number([4, 1, 2, 1, 2]) == 4


def test_single():
    assert single_number([1]) == 1


def test_negative():
    assert single_number([-1, -1, -2]) == -2


def test_larger():
    assert single_number([1, 2, 3, 4, 5, 4, 3, 2, 1]) == 5


def test_zero():
    assert single_number([0, 1, 0]) == 1


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single()
    test_negative()
    test_larger()
    test_zero()
    print("All tests passed!")
