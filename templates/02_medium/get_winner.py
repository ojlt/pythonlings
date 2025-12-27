"""
Tic-Tac-Toe Winner

Complete the function get_winner(board) to compute the winner of a game of
Tic-Tac-Toe given the state of a board.

board is a two-dimensional list representing an N x N grid, where N can be an
arbitrary number between 3 and 50 (both inclusive). Each cell can be filled
with either "x", "o" or " " (a blank space). You can assume that board is
always valid.

The function returns one of the following: "x", "o", "draw" or None.

The winner of the game is where either "x" or "o" has occupied N consecutive
grid cells in a single row, column or diagonal. If all cells are occupied
without a winner, return "draw". Otherwise, return None to indicate that the
game has not yet finished.

Examples:
    A 5x5 board with 'x' winning diagonally -> "x"
    A 4x4 board with all cells filled and no winner -> "draw"
    A 3x3 board with 'o' winning a row -> "o"
    A 7x7 board with empty cells and no winner yet -> None
"""

# I AM NOT DONE


def get_winner(board):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_x_wins_diagonal():
    board = [
        ['x', 'o', ' ', 'o', 'x'],
        ['x', 'x', 'o', ' ', ' '],
        ['o', 'o', 'x', ' ', ' '],
        [' ', 'o', 'o', 'x', 'o'],
        [' ', ' ', ' ', ' ', 'x']
    ]
    assert get_winner(board) == "x"


def test_draw():
    board = [
        ['o', 'x', 'o', 'x'],
        ['o', 'o', 'o', 'x'],
        ['x', 'x', 'x', 'o'],
        ['x', 'o', 'x', 'o']
    ]
    assert get_winner(board) == "draw"


def test_o_wins_row():
    board = [
        [' ', 'x', ' '],
        ['o', 'o', 'o'],
        ['x', 'x', ' ']
    ]
    assert get_winner(board) == "o"


def test_game_not_finished():
    board = [
        [' ', ' ', ' ', 'o', ' ', ' ', 'o'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['x', ' ', 'x', 'x', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['x', ' ', ' ', ' ', ' ', ' ', 'o']
    ]
    assert get_winner(board) is None


def test_x_wins_column():
    board = [
        ['x', 'o', 'o'],
        ['x', 'o', ' '],
        ['x', ' ', ' ']
    ]
    assert get_winner(board) == "x"


if __name__ == "__main__":
    test_x_wins_diagonal()
    test_draw()
    test_o_wins_row()
    test_game_not_finished()
    test_x_wins_column()
    print("All tests passed!")
