"""
Move Zeroes (LeetCode #283)

Given an integer array nums, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
The function should modify nums directly and return None.

Examples:
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    # nums is now [1, 3, 12, 0, 0]

    nums = [0]
    move_zeroes(nums)
    # nums is now [0]
"""

# I AM NOT DONE


def move_zeroes(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    nums = [0, 1, 0, 3, 12]
    move_zeroes(nums)
    assert nums == [1, 3, 12, 0, 0]


def test_single_zero():
    nums = [0]
    move_zeroes(nums)
    assert nums == [0]


def test_no_zeroes():
    nums = [1, 2, 3]
    move_zeroes(nums)
    assert nums == [1, 2, 3]


def test_all_zeroes():
    nums = [0, 0, 0]
    move_zeroes(nums)
    assert nums == [0, 0, 0]


def test_zeroes_at_end():
    nums = [1, 2, 0, 0]
    move_zeroes(nums)
    assert nums == [1, 2, 0, 0]


def test_zeroes_at_start():
    nums = [0, 0, 1, 2]
    move_zeroes(nums)
    assert nums == [1, 2, 0, 0]


if __name__ == "__main__":
    test_example1()
    test_single_zero()
    test_no_zeroes()
    test_all_zeroes()
    test_zeroes_at_end()
    test_zeroes_at_start()
    print("All tests passed!")
