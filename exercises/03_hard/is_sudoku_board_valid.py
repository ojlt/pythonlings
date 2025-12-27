"""
Sudoku Board Validator

Complete the function is_sudoku_board_valid(board) that returns a bool
indicating whether a given Sudoku board is valid.

board is a two-dimensional list of str representing a 9x9 grid. Each cell is
filled with a digit from "1" to "9" or a "." representing a blank cell.

A Sudoku board is valid only if all the following conditions are true:
- Each cell must be a valid string ("1" to "9" or ".")
- Each row does not have any duplicated digits
- Each column does not have any duplicated digits
- Each 3x3 box does not have any duplicated digits

You can assume that the size of board will always be 9 x 9.

Note: A valid board is not necessarily solvable. This function only checks
if the current configuration violates any Sudoku rules.
"""

# I AM NOT DONE


def is_sudoku_board_valid(board):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_valid_incomplete():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_sudoku_board_valid(board) == True


def test_valid_complete():
    board = [
        ["5", "3", "4", "6", "7", "8", "9", "1", "2"],
        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]
    ]
    assert is_sudoku_board_valid(board) == True


def test_invalid_row():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "5"],  # 5 appears twice
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_sudoku_board_valid(board) == False


def test_invalid_column():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        ["5", "9", "8", ".", ".", ".", ".", "6", "."],  # 5 in first column
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_sudoku_board_valid(board) == False


def test_invalid_box():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", "5", ".", "1", "9", "5", ".", ".", "."],  # 5 in top-left box
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    assert is_sudoku_board_valid(board) == False


if __name__ == "__main__":
    test_valid_incomplete()
    test_valid_complete()
    test_invalid_row()
    test_invalid_column()
    test_invalid_box()
    print("All tests passed!")
