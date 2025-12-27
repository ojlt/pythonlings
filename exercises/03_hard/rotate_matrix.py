"""
Rotate Matrix

Complete the function rotate_matrix(matrix) that rotates a given N x N 2D
list (matrix) by 90 degrees clockwise.

This operation must be done in-place. Do not create a new matrix to store
the result. The function should return None as it modifies the matrix directly.

You can assume the matrix is square (N x N).

Examples:
    Input matrix:
    [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9] ]

    After rotate_matrix(matrix) is called, matrix should be:
    [ [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3] ]

    Input matrix:
    [ [ 5,  1,  9, 11],
      [ 2,  4,  8, 10],
      [13,  3,  6,  7],
      [15, 14, 12, 16] ]

    After rotate_matrix(matrix) is called, matrix should be:
    [ [15, 13,  2,  5],
      [14,  3,  4,  1],
      [12,  6,  8,  9],
      [16,  7, 10, 11] ]
"""

# I AM NOT DONE


def rotate_matrix(matrix):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_3x3():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    rotate_matrix(matrix)
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    assert matrix == expected


def test_4x4():
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    rotate_matrix(matrix)
    expected = [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11]
    ]
    assert matrix == expected


def test_2x2():
    matrix = [
        [1, 2],
        [3, 4]
    ]
    rotate_matrix(matrix)
    expected = [
        [3, 1],
        [4, 2]
    ]
    assert matrix == expected


def test_1x1():
    matrix = [[1]]
    rotate_matrix(matrix)
    expected = [[1]]
    assert matrix == expected


if __name__ == "__main__":
    test_3x3()
    test_4x4()
    test_2x2()
    test_1x1()
    print("All tests passed!")
