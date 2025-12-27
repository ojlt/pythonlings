"""
Min Max Swap

Complete the function minmax_swap(number) that swaps two digits in a given
number (an int).

The function should return a tuple with two elements:
- The first element is the smallest int that can be obtained by swapping
  any two digits in number.
- The second element is the largest int that can be obtained by swapping
  any two digits in number.

If number is the smallest (or largest) after all possible swaps, then keep
the number unswapped.

All numbers after swapping must not have leading zeros, e.g. 05432 is invalid.

You can assume that number will always be a positive integer and with no
leading zeros.

Examples:
    minmax_swap(31572) -> (13572, 71532)
    minmax_swap(91213) -> (11293, 93211)
    minmax_swap(9876) -> (6879, 9876)  # Number itself is already max
    minmax_swap(27) -> (27, 72)
    minmax_swap(400) -> (400, 400)  # No swapping can occur
    minmax_swap(5) -> (5, 5)  # No swapping can occur
"""

# I AM NOT DONE


def minmax_swap(number):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_5_digits():
    output = minmax_swap(31572)
    expected_output = (13572, 71532)
    assert output == expected_output


def test_repeated_digits():
    output = minmax_swap(91213)
    expected_output = (11293, 93211)
    assert output == expected_output


def test_no_max_swap():
    output = minmax_swap(9876)
    expected_output = (6879, 9876)
    assert output == expected_output


def test_two_digits():
    output = minmax_swap(27)
    expected_output = (27, 72)
    assert output == expected_output


def test_no_leading_zeros():
    output = minmax_swap(400)
    expected_output = (400, 400)
    assert output == expected_output


def test_single_digit():
    output = minmax_swap(5)
    expected_output = (5, 5)
    assert output == expected_output


if __name__ == "__main__":
    test_5_digits()
    test_repeated_digits()
    test_no_max_swap()
    test_two_digits()
    test_no_leading_zeros()
    test_single_digit()
    print("All tests passed!")
