"""
Trapping Rain Water (LeetCode #42)

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it can trap after raining.

Examples:
    trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) -> 6
        # The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]
        # In this case, 6 units of rain water are being trapped.

    trap([4, 2, 0, 3, 2, 5]) -> 9
"""

# I AM NOT DONE


def trap(height):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6


def test_example2():
    assert trap([4, 2, 0, 3, 2, 5]) == 9


def test_empty():
    assert trap([]) == 0


def test_no_trap():
    assert trap([1, 2, 3, 4, 5]) == 0


def test_no_trap_decreasing():
    assert trap([5, 4, 3, 2, 1]) == 0


def test_single():
    assert trap([5]) == 0


def test_two_elements():
    assert trap([5, 2]) == 0


def test_simple_valley():
    assert trap([3, 0, 3]) == 3


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_empty()
    test_no_trap()
    test_no_trap_decreasing()
    test_single()
    test_two_elements()
    test_simple_valley()
    print("All tests passed!")
