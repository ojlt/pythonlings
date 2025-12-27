"""
Search in Rotated Sorted Array (LeetCode #33)

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array is
[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]].

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become
[4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return
the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Examples:
    search([4, 5, 6, 7, 0, 1, 2], 0) -> 4
    search([4, 5, 6, 7, 0, 1, 2], 3) -> -1
    search([1], 0) -> -1
"""

# I AM NOT DONE


def search(nums, target):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_example2():
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_single_not_found():
    assert search([1], 0) == -1


def test_single_found():
    assert search([1], 1) == 0


def test_not_rotated():
    assert search([1, 2, 3, 4, 5], 3) == 2


def test_find_first():
    assert search([4, 5, 6, 7, 0, 1, 2], 4) == 0


def test_find_last():
    assert search([4, 5, 6, 7, 0, 1, 2], 2) == 6


def test_two_elements():
    assert search([3, 1], 1) == 1


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single_not_found()
    test_single_found()
    test_not_rotated()
    test_find_first()
    test_find_last()
    test_two_elements()
    print("All tests passed!")
