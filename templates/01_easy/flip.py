"""
Flip Grid

Complete the function flip(grid) that flips the values in grid from 0 to 1
and from 1 to 0.

You can assume that grid is always a two-dimensional list of any width or
height (at least 1x1). Each row will have the same width, and each column
the same height.

You can also assume that the value of each grid cell can either only be 0 or 1.

Examples:
    flip([[0]]) -> [[1]]
    flip([[0, 1], [1, 0]]) -> [[1, 0], [0, 1]]
    flip([[1, 1, 0, 0], [0, 1, 0, 1]]) -> [[0, 0, 1, 1], [1, 0, 1, 0]]
"""

# I AM NOT DONE


def flip(grid):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_1x1_grid():
    grid = [[0]]
    result = flip(grid)
    expected = [[1]]
    assert result == expected


def test_2x2_grid():
    grid = [[0, 1], [1, 0]]
    result = flip(grid)
    expected = [[1, 0], [0, 1]]
    assert result == expected


def test_2x4_grid():
    grid = [[1, 1, 0, 0], [0, 1, 0, 1]]
    result = flip(grid)
    expected = [[0, 0, 1, 1], [1, 0, 1, 0]]
    assert result == expected


def test_5x2_grid():
    grid = [[0, 0], [0, 0], [0, 0], [1, 1], [1, 1]]
    result = flip(grid)
    expected = [[1, 1], [1, 1], [1, 1], [0, 0], [0, 0]]
    assert result == expected


def test_5x5_grid():
    grid = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1],
    ]
    result = flip(grid)
    expected = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
    ]
    assert result == expected


if __name__ == "__main__":
    test_1x1_grid()
    test_2x2_grid()
    test_2x4_grid()
    test_5x2_grid()
    test_5x5_grid()
    print("All tests passed!")
