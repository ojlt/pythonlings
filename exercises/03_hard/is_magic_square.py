"""
Magic Square

Complete the function is_magic_square(matrix) that returns a bool indicating
whether a given matrix is a magic square.

A 2D matrix of size N x N is a magic square if:
- the matrix is made up of positive integers 1 to N^2 (inclusive);
- each integer in the matrix only occurs once (no repeats); and
- the sum of the numbers in each row, each column and both main diagonals are
  all the same (they all sum to a common "magic constant").

matrix is a two-dimensional list of int representing a square N x N grid,
where N is any positive integer. You can assume that the matrix will always
be in a valid format.

Examples:
    is_magic_square([[1]]) -> True
    is_magic_square([[5]]) -> False  (max integer is 1 for a 1x1 matrix)
    is_magic_square([[8, 1, 6], [3, 5, 7], [4, 9, 2]]) -> True
    is_magic_square([[8, 11, 6], [3, 5, 7], [4, 9, 2]]) -> False  (11 out of range)
    is_magic_square([[8, 1, 7], [3, 5, 7], [4, 9, 2]]) -> False  (7 repeated)
"""

# I AM NOT DONE


def is_magic_square(matrix):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_1x1_valid():
    matrix = [[1]]
    assert is_magic_square(matrix) == True


def test_1x1_invalid():
    matrix = [[5]]
    assert is_magic_square(matrix) == False


def test_3x3_valid():
    matrix = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    assert is_magic_square(matrix) == True


def test_3x3_out_of_range():
    matrix = [
        [8, 11, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    assert is_magic_square(matrix) == False


def test_3x3_repeated():
    matrix = [
        [8, 1, 7],
        [3, 5, 7],
        [4, 9, 2]
    ]
    assert is_magic_square(matrix) == False


def test_3x3_wrong_sum():
    matrix = [
        [8, 2, 6],
        [3, 5, 7],
        [4, 9, 1]
    ]
    assert is_magic_square(matrix) == False


def test_3x3_diagonal_wrong():
    matrix = [
        [1, 5, 9],
        [6, 7, 2],
        [8, 3, 4]
    ]
    assert is_magic_square(matrix) == False


def test_6x6_valid():
    matrix = [
        [35, 1, 6, 26, 19, 24],
        [3, 32, 7, 21, 23, 25],
        [31, 9, 2, 22, 27, 20],
        [8, 28, 33, 17, 10, 15],
        [30, 5, 34, 12, 14, 16],
        [4, 36, 29, 13, 18, 11]
    ]
    assert is_magic_square(matrix) == True


if __name__ == "__main__":
    test_1x1_valid()
    test_1x1_invalid()
    test_3x3_valid()
    test_3x3_out_of_range()
    test_3x3_repeated()
    test_3x3_wrong_sum()
    test_3x3_diagonal_wrong()
    test_6x6_valid()
    print("All tests passed!")
