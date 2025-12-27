"""
Container With Most Water (LeetCode #11)

You are given an integer array height of length n. There are n vertical lines
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the
container contains the most water.

Return the maximum amount of water a container can store.

Note: You may not slant the container.

Examples:
    max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) -> 49
        # Lines at index 1 (height 8) and index 8 (height 7)
        # Area = min(8, 7) * (8 - 1) = 7 * 7 = 49
    max_area([1, 1]) -> 1
"""

# I AM NOT DONE


def max_area(height):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_example2():
    assert max_area([1, 1]) == 1


def test_increasing():
    assert max_area([1, 2, 3, 4, 5]) == 6


def test_decreasing():
    assert max_area([5, 4, 3, 2, 1]) == 6


def test_same_height():
    assert max_area([5, 5, 5, 5]) == 15


def test_two_tall():
    assert max_area([1, 100, 1, 1, 1, 100, 1]) == 500


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_increasing()
    test_decreasing()
    test_same_height()
    test_two_tall()
    print("All tests passed!")
