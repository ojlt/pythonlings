"""
Two Sum (LeetCode #1)

Given an array of integers nums and an integer target, return indices of the
two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may
not use the same element twice.

You can return the answer in any order.

Examples:
    two_sum([2, 7, 11, 15], 9) -> [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9
    two_sum([3, 2, 4], 6) -> [1, 2]
    two_sum([3, 3], 6) -> [0, 1]
"""

# I AM NOT DONE


def two_sum(nums, target):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    result = two_sum([2, 7, 11, 15], 9)
    assert sorted(result) == [0, 1]


def test_example2():
    result = two_sum([3, 2, 4], 6)
    assert sorted(result) == [1, 2]


def test_example3():
    result = two_sum([3, 3], 6)
    assert sorted(result) == [0, 1]


def test_negative():
    result = two_sum([-1, -2, -3, -4, -5], -8)
    assert sorted(result) == [2, 4]


def test_large():
    result = two_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 19)
    assert sorted(result) == [8, 9]


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_example3()
    test_negative()
    test_large()
    print("All tests passed!")
