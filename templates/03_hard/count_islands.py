"""
Count Islands

Complete the function count_islands(grid). This function takes a 2D list
(grid) of strings, where "1" represents land and "0" represents water.

The function should return an integer count of the number of "islands."
An island is formed by connecting adjacent "1"s horizontally or vertically
(not diagonally). You can assume all four edges of the grid are surrounded
by water.

Examples:
    Input grid:
    [ ["1", "1", "1", "1", "0"],
      ["1", "1", "0", "1", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "0", "0", "0"] ]
    count_islands(grid) should return: 1

    Input grid:
    [ ["1", "1", "0", "0", "0"],
      ["1", "1", "0", "0", "0"],
      ["0", "0", "1", "0", "0"],
      ["0", "0", "0", "1", "1"] ]
    count_islands(grid) should return: 3
"""

# I AM NOT DONE


def count_islands(grid):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_one_island():
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert count_islands(grid) == 1


def test_three_islands():
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert count_islands(grid) == 3


def test_no_islands():
    grid = [
        ["0", "0", "0"],
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    assert count_islands(grid) == 0


def test_all_land():
    grid = [
        ["1", "1", "1"],
        ["1", "1", "1"],
        ["1", "1", "1"]
    ]
    assert count_islands(grid) == 1


def test_diagonal_not_connected():
    grid = [
        ["1", "0", "1"],
        ["0", "1", "0"],
        ["1", "0", "1"]
    ]
    assert count_islands(grid) == 5


if __name__ == "__main__":
    test_one_island()
    test_three_islands()
    test_no_islands()
    test_all_land()
    test_diagonal_not_connected()
    print("All tests passed!")
