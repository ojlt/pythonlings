"""
House Robber (LeetCode #198)

You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security systems
connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting
the police.

Examples:
    rob([1, 2, 3, 1]) -> 4
        # Rob house 1 (money = 1) and then rob house 3 (money = 3)
        # Total = 1 + 3 = 4
    rob([2, 7, 9, 3, 1]) -> 12
        # Rob house 1 (money = 2), house 3 (money = 9), house 5 (money = 1)
        # Total = 2 + 9 + 1 = 12
"""

# I AM NOT DONE


def rob(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert rob([1, 2, 3, 1]) == 4


def test_example2():
    assert rob([2, 7, 9, 3, 1]) == 12


def test_single():
    assert rob([5]) == 5


def test_two_houses():
    assert rob([1, 2]) == 2


def test_empty():
    assert rob([]) == 0


def test_all_same():
    assert rob([5, 5, 5, 5, 5]) == 15


def test_decreasing():
    assert rob([10, 5, 3, 1]) == 13


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single()
    test_two_houses()
    test_empty()
    test_all_same()
    test_decreasing()
    print("All tests passed!")
