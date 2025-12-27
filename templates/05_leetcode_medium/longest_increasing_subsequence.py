"""
Longest Increasing Subsequence (LeetCode #300)

Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting
some or no elements without changing the order of the remaining elements.

Examples:
    length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) -> 4
        # The longest increasing subsequence is [2, 3, 7, 101], length = 4
    length_of_lis([0, 1, 0, 3, 2, 3]) -> 4
        # The longest increasing subsequence is [0, 1, 2, 3], length = 4
    length_of_lis([7, 7, 7, 7, 7, 7, 7]) -> 1
        # All elements are the same, so the longest is just one element
"""

# I AM NOT DONE


def length_of_lis(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4


def test_example2():
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4


def test_all_same():
    assert length_of_lis([7, 7, 7, 7, 7, 7, 7]) == 1


def test_increasing():
    assert length_of_lis([1, 2, 3, 4, 5]) == 5


def test_decreasing():
    assert length_of_lis([5, 4, 3, 2, 1]) == 1


def test_single():
    assert length_of_lis([10]) == 1


def test_empty():
    assert length_of_lis([]) == 0


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_all_same()
    test_increasing()
    test_decreasing()
    test_single()
    test_empty()
    print("All tests passed!")
