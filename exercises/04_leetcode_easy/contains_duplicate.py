"""
Contains Duplicate (LeetCode #217)

Given an integer array nums, return True if any value appears at least
twice in the array, and return False if every element is distinct.

Examples:
    contains_duplicate([1, 2, 3, 1]) -> True
    contains_duplicate([1, 2, 3, 4]) -> False
    contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) -> True
"""

# I AM NOT DONE


def contains_duplicate(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_has_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) == True


def test_no_duplicate():
    assert contains_duplicate([1, 2, 3, 4]) == False


def test_many_duplicates():
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True


def test_empty():
    assert contains_duplicate([]) == False


def test_single():
    assert contains_duplicate([1]) == False


def test_two_same():
    assert contains_duplicate([1, 1]) == True


def test_two_different():
    assert contains_duplicate([1, 2]) == False


if __name__ == "__main__":
    test_has_duplicate()
    test_no_duplicate()
    test_many_duplicates()
    test_empty()
    test_single()
    test_two_same()
    test_two_different()
    print("All tests passed!")
