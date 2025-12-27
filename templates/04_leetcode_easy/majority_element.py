"""
Majority Element (LeetCode #169)

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than n/2 times.
You may assume that the majority element always exists in the array.

Examples:
    majority_element([3, 2, 3]) -> 3
    majority_element([2, 2, 1, 1, 1, 2, 2]) -> 2
"""

# I AM NOT DONE


def majority_element(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert majority_element([3, 2, 3]) == 3


def test_example2():
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2


def test_single():
    assert majority_element([1]) == 1


def test_all_same():
    assert majority_element([5, 5, 5, 5]) == 5


def test_two_elements():
    assert majority_element([1, 1, 2]) == 1


def test_larger():
    assert majority_element([1, 1, 1, 2, 2, 1, 1]) == 1


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single()
    test_all_same()
    test_two_elements()
    test_larger()
    print("All tests passed!")
