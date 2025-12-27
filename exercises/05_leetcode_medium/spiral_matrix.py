"""
Spiral Matrix (LeetCode #54)

Given an m x n matrix, return all elements of the matrix in spiral order.

Spiral order means: start at top-left, go right, then down, then left,
then up, and repeat inward.

Examples:
    spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> [1,2,3,6,9,8,7,4,5]
    spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        -> [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# I AM NOT DONE


def spiral_order(matrix):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_order(matrix) == [1, 2, 3, 6, 9, 8, 7, 4, 5]


def test_example2():
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    assert spiral_order(matrix) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]


def test_single_row():
    assert spiral_order([[1, 2, 3]]) == [1, 2, 3]


def test_single_column():
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]


def test_single_cell():
    assert spiral_order([[1]]) == [1]


def test_empty():
    assert spiral_order([]) == []


def test_2x2():
    assert spiral_order([[1, 2], [3, 4]]) == [1, 2, 4, 3]


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single_row()
    test_single_column()
    test_single_cell()
    test_empty()
    test_2x2()
    print("All tests passed!")
