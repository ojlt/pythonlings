"""
First Missing Positive (LeetCode #41)

Given an unsorted integer array nums, return the smallest positive integer
that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1)
auxiliary space.

Examples:
    first_missing_positive([1, 2, 0]) -> 3
        # 1 and 2 are present, so the answer is 3
    first_missing_positive([3, 4, -1, 1]) -> 2
        # 1 is present but 2 is missing
    first_missing_positive([7, 8, 9, 11, 12]) -> 1
        # 1 is the smallest positive missing
"""

# I AM NOT DONE


def first_missing_positive(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert first_missing_positive([1, 2, 0]) == 3


def test_example2():
    assert first_missing_positive([3, 4, -1, 1]) == 2


def test_example3():
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1


def test_single_one():
    assert first_missing_positive([1]) == 2


def test_single_two():
    assert first_missing_positive([2]) == 1


def test_consecutive():
    assert first_missing_positive([1, 2, 3, 4, 5]) == 6


def test_empty():
    assert first_missing_positive([]) == 1


def test_duplicates():
    assert first_missing_positive([1, 1, 1, 1]) == 2


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_example3()
    test_single_one()
    test_single_two()
    test_consecutive()
    test_empty()
    test_duplicates()
    print("All tests passed!")
