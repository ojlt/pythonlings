"""
Missing Number (LeetCode #268)

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Examples:
    missing_number([3, 0, 1]) -> 2
        # n = 3, range is [0, 1, 2, 3], missing 2
    missing_number([0, 1]) -> 2
        # n = 2, range is [0, 1, 2], missing 2
    missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) -> 8
        # n = 9, range is [0-9], missing 8
"""

# I AM NOT DONE


def missing_number(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert missing_number([3, 0, 1]) == 2


def test_example2():
    assert missing_number([0, 1]) == 2


def test_example3():
    assert missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8


def test_missing_zero():
    assert missing_number([1, 2, 3]) == 0


def test_missing_last():
    assert missing_number([0, 1, 2]) == 3


def test_single_zero():
    assert missing_number([0]) == 1


def test_single_one():
    assert missing_number([1]) == 0


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_example3()
    test_missing_zero()
    test_missing_last()
    test_single_zero()
    test_single_one()
    print("All tests passed!")
