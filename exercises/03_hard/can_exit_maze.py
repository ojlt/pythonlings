"""
Maze Solver

Complete the function can_exit_maze(maze) that returns a bool indicating
whether there is a valid path in a given maze where you can navigate from
its entrance to the exit.

A maze is an M x N matrix with elements that can either be 0 or 1. A 0
indicates a walkable area, and a 1 indicates a wall. The entrance of the maze
is always at the upper-left corner, and the exit is always at the bottom-right
corner. You can only navigate up, down, left, and right (and NOT diagonally).

You can assume that maze is always a two-dimensional list of any width or
height (and will always be at least 2 x 2). Each row will have the same width,
and each column the same height. You may also assume that there is always an
entrance (maze[0][0] will always be 0), although there may not always be an exit.

You can also assume that the value of each cell in maze will always either
only be the integers 0 or 1.

Examples:
    can_exit_maze([[0, 1, 0, 0, 1, 1],
                   [0, 0, 0, 1, 0, 0],
                   [1, 1, 0, 0, 0, 1],
                   [1, 1, 1, 1, 0, 0]]) -> True
    can_exit_maze([[0, 1],
                   [1, 0]]) -> False
"""

# I AM NOT DONE


def can_exit_maze(maze):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_solvable():
    maze = [
        [0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 0]
    ]
    assert can_exit_maze(maze) == True


def test_blocked():
    maze = [
        [0, 1, 0, 0, 1, 1],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0]
    ]
    assert can_exit_maze(maze) == False


def test_vertical():
    maze = [
        [0, 1, 1, 0],
        [0, 1, 1, 1],
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
    ]
    assert can_exit_maze(maze) == True


def test_no_exit():
    maze = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    assert can_exit_maze(maze) == False


def test_simple_true():
    maze = [
        [0, 1],
        [0, 0]
    ]
    assert can_exit_maze(maze) == True


def test_simple_false():
    maze = [
        [0, 1],
        [1, 0]
    ]
    assert can_exit_maze(maze) == False


if __name__ == "__main__":
    test_solvable()
    test_blocked()
    test_vertical()
    test_no_exit()
    test_simple_true()
    test_simple_false()
    print("All tests passed!")
