"""
Longest Consecutive Sequence (LeetCode #128)

Given an unsorted array of integers nums, return the length of the longest
consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Examples:
    longest_consecutive([100, 4, 200, 1, 3, 2]) -> 4
        # The longest consecutive sequence is [1, 2, 3, 4], length = 4
    longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) -> 9
        # The longest consecutive sequence is [0, 1, 2, 3, 4, 5, 6, 7, 8]
"""

# I AM NOT DONE


def longest_consecutive(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_example2():
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9


def test_empty():
    assert longest_consecutive([]) == 0


def test_single():
    assert longest_consecutive([5]) == 1


def test_duplicates():
    assert longest_consecutive([1, 2, 2, 3]) == 3


def test_no_consecutive():
    assert longest_consecutive([10, 20, 30, 40]) == 1


def test_negative():
    assert longest_consecutive([-1, 0, 1, 2]) == 4


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_empty()
    test_single()
    test_duplicates()
    test_no_consecutive()
    test_negative()
    print("All tests passed!")
