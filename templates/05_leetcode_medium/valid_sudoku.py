"""
Valid Sudoku (LeetCode #36)

Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes must contain digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not necessarily solvable.
- Only the filled cells need to be validated.
- Empty cells are represented by '.'.

Examples:
    is_valid_sudoku([
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]) -> True
"""

# I AM NOT DONE


def is_valid_sudoku(board):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_valid_board():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku(board) == True


def test_invalid_row():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        ["5",".",".",".","8",".",".","7","9"]  # 5 appears twice in column 1
    ]
    assert is_valid_sudoku(board) == False


def test_invalid_box():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6","5",".","1","9","5",".",".","."],  # 5 in same 3x3 box
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    assert is_valid_sudoku(board) == False


def test_empty_board():
    board = [["." for _ in range(9)] for _ in range(9)]
    assert is_valid_sudoku(board) == True


if __name__ == "__main__":
    test_valid_board()
    test_invalid_row()
    test_invalid_box()
    test_empty_board()
    print("All tests passed!")
