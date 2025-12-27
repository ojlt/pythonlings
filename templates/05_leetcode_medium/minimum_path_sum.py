"""
Minimum Path Sum (LeetCode #64)

Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Examples:
    min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) -> 7
        # Path: 1 -> 3 -> 1 -> 1 -> 1 = 7
    min_path_sum([[1, 2, 3], [4, 5, 6]]) -> 12
        # Path: 1 -> 2 -> 3 -> 6 = 12
"""

# I AM NOT DONE


def min_path_sum(grid):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]) == 7


def test_example2():
    assert min_path_sum([[1, 2, 3], [4, 5, 6]]) == 12


def test_single_cell():
    assert min_path_sum([[5]]) == 5


def test_single_row():
    assert min_path_sum([[1, 2, 3]]) == 6


def test_single_column():
    assert min_path_sum([[1], [2], [3]]) == 6


def test_all_ones():
    assert min_path_sum([[1, 1], [1, 1]]) == 3


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single_cell()
    test_single_row()
    test_single_column()
    test_all_ones()
    print("All tests passed!")
