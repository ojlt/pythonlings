"""
3Sum (LeetCode #15)

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Examples:
    three_sum([-1, 0, 1, 2, -1, -4]) -> [[-1, -1, 2], [-1, 0, 1]]
    three_sum([0, 1, 1]) -> []
    three_sum([0, 0, 0]) -> [[0, 0, 0]]
"""

# I AM NOT DONE


def three_sum(nums):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    result = three_sum([-1, 0, 1, 2, -1, -4])
    expected = [[-1, -1, 2], [-1, 0, 1]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


def test_no_solution():
    assert three_sum([0, 1, 1]) == []


def test_all_zeros():
    result = three_sum([0, 0, 0])
    assert result == [[0, 0, 0]]


def test_empty():
    assert three_sum([]) == []


def test_two_elements():
    assert three_sum([1, -1]) == []


def test_multiple_solutions():
    result = three_sum([-2, 0, 1, 1, 2])
    expected = [[-2, 0, 2], [-2, 1, 1]]
    assert sorted([sorted(x) for x in result]) == sorted([sorted(x) for x in expected])


if __name__ == "__main__":
    test_example1()
    test_no_solution()
    test_all_zeros()
    test_empty()
    test_two_elements()
    test_multiple_solutions()
    print("All tests passed!")
