"""
Climbing Stairs (LeetCode #70)

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways
can you climb to the top?

Examples:
    climb_stairs(2) -> 2
        # Two ways: (1+1) or (2)
    climb_stairs(3) -> 3
        # Three ways: (1+1+1), (1+2), (2+1)
    climb_stairs(4) -> 5
        # Five ways: (1+1+1+1), (1+1+2), (1+2+1), (2+1+1), (2+2)
"""

# I AM NOT DONE


def climb_stairs(n):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_one_step():
    assert climb_stairs(1) == 1


def test_two_steps():
    assert climb_stairs(2) == 2


def test_three_steps():
    assert climb_stairs(3) == 3


def test_four_steps():
    assert climb_stairs(4) == 5


def test_five_steps():
    assert climb_stairs(5) == 8


def test_ten_steps():
    assert climb_stairs(10) == 89


if __name__ == "__main__":
    test_one_step()
    test_two_steps()
    test_three_steps()
    test_four_steps()
    test_five_steps()
    test_ten_steps()
    print("All tests passed!")
