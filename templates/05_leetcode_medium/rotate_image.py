"""
Rotate Image (LeetCode #48)

You are given an n x n 2D matrix representing an image, rotate the image
by 90 degrees clockwise.

You have to rotate the image in-place, which means you have to modify the
input 2D matrix directly. DO NOT allocate another 2D matrix and do the
rotation.

The function should return None and modify the matrix in place.

Examples:
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    # matrix is now [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix)
    # matrix is now [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
"""

# I AM NOT DONE


def rotate(matrix):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_3x3():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(matrix)
    assert matrix == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


def test_4x4():
    matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    rotate(matrix)
    assert matrix == [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]


def test_1x1():
    matrix = [[1]]
    rotate(matrix)
    assert matrix == [[1]]


def test_2x2():
    matrix = [[1, 2], [3, 4]]
    rotate(matrix)
    assert matrix == [[3, 1], [4, 2]]


if __name__ == "__main__":
    test_3x3()
    test_4x4()
    test_1x1()
    test_2x2()
    print("All tests passed!")
