"""
TicTacToe Game Class

Complete the TicTacToeGame class. This class should manage the state and
logic of an N x N Tic-Tac-Toe game.

You must implement the following:

1. __init__(self, n=3):
   - Initializes the game.
   - self.n: The size of the board (N).
   - self.board: A 2D list of size N x N, initialized with spaces (" ").
   - self.current_player: Set to "x".

2. move(self, r, c):
   - Takes a row r and column c for the current player's move.
   - If r or c are out of bounds (not 0 <= index < N), it should raise a
     ValueError("Move out of bounds.").
   - If the cell self.board[r][c] is not a space (" "), it should raise a
     ValueError("Cell already occupied.").
   - If the move is valid: Place the self.current_player's mark ("x" or "o")
     in self.board[r][c]. Switch the self.current_player.
   - The function should return None.

3. get_winner(self):
   - This method analyzes self.board to determine the game's state.
   - It should return one of the following strings: "x", "o", "draw"
     (if the board is full without a winner), or None (if the game has
     not yet finished).
   - Note: You only need to check the two main diagonals (top-left to
     bottom-right, and top-right to bottom-left).
"""

# I AM NOT DONE


class TicTacToeGame:
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
import pytest


def test_init():
    game = TicTacToeGame(3)
    assert game.n == 3
    assert game.current_player == "x"
    assert len(game.board) == 3
    assert all(len(row) == 3 for row in game.board)
    assert all(cell == " " for row in game.board for cell in row)


def test_move():
    game = TicTacToeGame(3)
    game.move(0, 0)
    assert game.board[0][0] == "x"
    assert game.current_player == "o"

    game.move(1, 1)
    assert game.board[1][1] == "o"
    assert game.current_player == "x"


def test_invalid_move_out_of_bounds():
    game = TicTacToeGame(3)
    try:
        game.move(3, 0)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Move out of bounds."


def test_invalid_move_occupied():
    game = TicTacToeGame(3)
    game.move(0, 0)
    try:
        game.move(0, 0)
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert str(e) == "Cell already occupied."


def test_x_wins():
    game = TicTacToeGame(3)
    game.move(0, 0)  # x
    game.move(1, 0)  # o
    game.move(0, 1)  # x
    game.move(1, 1)  # o
    game.move(0, 2)  # x wins
    assert game.get_winner() == "x"


def test_o_wins():
    game = TicTacToeGame(3)
    game.move(0, 0)  # x
    game.move(1, 0)  # o
    game.move(0, 1)  # x
    game.move(1, 1)  # o
    game.move(2, 2)  # x
    game.move(1, 2)  # o wins
    assert game.get_winner() == "o"


def test_draw():
    game = TicTacToeGame(3)
    # x o x
    # x x o
    # o x o
    game.move(0, 0)  # x
    game.move(0, 1)  # o
    game.move(0, 2)  # x
    game.move(1, 2)  # o
    game.move(1, 0)  # x
    game.move(2, 0)  # o
    game.move(1, 1)  # x
    game.move(2, 2)  # o
    game.move(2, 1)  # x
    assert game.get_winner() == "draw"


def test_game_not_finished():
    game = TicTacToeGame(3)
    game.move(0, 0)
    game.move(1, 1)
    assert game.get_winner() is None


if __name__ == "__main__":
    test_init()
    test_move()
    test_invalid_move_out_of_bounds()
    test_invalid_move_occupied()
    test_x_wins()
    test_o_wins()
    test_draw()
    test_game_not_finished()
    print("All tests passed!")
