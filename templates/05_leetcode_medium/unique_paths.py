"""
Unique Paths (LeetCode #62)

There is a robot on an m x n grid. The robot is initially located at the
top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right
corner (i.e., grid[m-1][n-1]). The robot can only move either down or right
at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

Examples:
    unique_paths(3, 7) -> 28
    unique_paths(3, 2) -> 3
        # From top-left to bottom-right, there are 3 ways:
        # Right -> Down -> Down
        # Down -> Down -> Right
        # Down -> Right -> Down
"""

# I AM NOT DONE


def unique_paths(m, n):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert unique_paths(3, 7) == 28


def test_example2():
    assert unique_paths(3, 2) == 3


def test_single_cell():
    assert unique_paths(1, 1) == 1


def test_single_row():
    assert unique_paths(1, 5) == 1


def test_single_column():
    assert unique_paths(5, 1) == 1


def test_square():
    assert unique_paths(3, 3) == 6


def test_larger():
    assert unique_paths(7, 3) == 28


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single_cell()
    test_single_row()
    test_single_column()
    test_square()
    test_larger()
    print("All tests passed!")
