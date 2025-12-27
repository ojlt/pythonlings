"""
Product of Array Except Self (LeetCode #238)

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Examples:
    product_except_self([1, 2, 3, 4]) -> [24, 12, 8, 6]
    product_except_self([-1, 1, 0, -3, 3]) -> [0, 0, 9, 0, 0]
"""

# I AM NOT DONE


def product_except_self(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]


def test_example2():
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]


def test_two_elements():
    assert product_except_self([2, 3]) == [3, 2]


def test_with_ones():
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]


def test_negative():
    assert product_except_self([-1, -2, -3]) == [6, 3, 2]


def test_single_zero():
    assert product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_two_elements()
    test_with_ones()
    test_negative()
    test_single_zero()
    print("All tests passed!")
