"""
Maximum Subarray (LeetCode #53)

Given an integer array nums, find the subarray with the largest sum,
and return its sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Examples:
    max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> 6
        # The subarray [4, -1, 2, 1] has the largest sum = 6
    max_subarray([1]) -> 1
        # Only one element
    max_subarray([5, 4, -1, 7, 8]) -> 23
        # The entire array has the largest sum

Hint: This is a classic problem solvable with Kadane's algorithm.
"""

# I AM NOT DONE


def max_subarray(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_example2():
    assert max_subarray([1]) == 1


def test_example3():
    assert max_subarray([5, 4, -1, 7, 8]) == 23


def test_all_negative():
    assert max_subarray([-3, -2, -5, -1]) == -1


def test_all_positive():
    assert max_subarray([1, 2, 3, 4]) == 10


def test_single_negative():
    assert max_subarray([-5]) == -5


def test_alternating():
    assert max_subarray([2, -1, 2, -1, 2]) == 4


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_example3()
    test_all_negative()
    test_all_positive()
    test_single_negative()
    test_alternating()
    print("All tests passed!")
