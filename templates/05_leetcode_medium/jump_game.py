"""
Jump Game (LeetCode #55)

You are given an integer array nums. You are initially positioned at the
array's first index, and each element in the array represents your maximum
jump length at that position.

Return True if you can reach the last index, or False otherwise.

Examples:
    can_jump([2, 3, 1, 1, 4]) -> True
        # Jump 1 step from index 0 to 1, then 3 steps to the last index
    can_jump([3, 2, 1, 0, 4]) -> False
        # You will always arrive at index 3, and cannot proceed
"""

# I AM NOT DONE


def can_jump(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert can_jump([2, 3, 1, 1, 4]) == True


def test_example2():
    assert can_jump([3, 2, 1, 0, 4]) == False


def test_single():
    assert can_jump([0]) == True


def test_two_reachable():
    assert can_jump([1, 0]) == True


def test_two_unreachable():
    assert can_jump([0, 1]) == False


def test_large_first():
    assert can_jump([10, 0, 0, 0, 0]) == True


def test_all_ones():
    assert can_jump([1, 1, 1, 1, 1]) == True


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single()
    test_two_reachable()
    test_two_unreachable()
    test_large_first()
    test_all_ones()
    print("All tests passed!")
