"""
Set Matrix Zeroes (LeetCode #73)

Given an m x n integer matrix, if an element is 0, set its entire row
and column to 0's.

You must do it in place (modify the matrix directly, return None).

Examples:
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix)
    # matrix is now [[1, 0, 1], [0, 0, 0], [1, 0, 1]]

    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(matrix)
    # matrix is now [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
"""

# I AM NOT DONE


def set_zeroes(matrix):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(matrix)
    assert matrix == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]


def test_example2():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(matrix)
    assert matrix == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]


def test_no_zeroes():
    matrix = [[1, 2], [3, 4]]
    set_zeroes(matrix)
    assert matrix == [[1, 2], [3, 4]]


def test_all_zeroes():
    matrix = [[0, 0], [0, 0]]
    set_zeroes(matrix)
    assert matrix == [[0, 0], [0, 0]]


def test_single_cell_zero():
    matrix = [[0]]
    set_zeroes(matrix)
    assert matrix == [[0]]


def test_single_cell_nonzero():
    matrix = [[5]]
    set_zeroes(matrix)
    assert matrix == [[5]]


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_no_zeroes()
    test_all_zeroes()
    test_single_cell_zero()
    test_single_cell_nonzero()
    print("All tests passed!")
