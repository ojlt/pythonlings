"""
Convert Seconds

Complete the function convert(seconds) that converts seconds (an int)
to an hour/minute/second format.

The function should return a tuple (hours, minutes, seconds).

You can assume that seconds will always be a non-negative integer.

Examples:
    convert(38) -> (0, 0, 38)
    convert(176) -> (0, 2, 56)
    convert(3823) -> (1, 3, 43)
    convert(0) -> (0, 0, 0)
"""

# I AM NOT DONE


def convert(seconds):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_second():
    output = convert(38)
    expected_output = (0, 0, 38)
    assert output == expected_output


def test_minute():
    output = convert(176)
    expected_output = (0, 2, 56)
    assert output == expected_output


def test_hour():
    output = convert(3823)
    expected_output = (1, 3, 43)
    assert output == expected_output


def test_zero():
    output = convert(0)
    expected_output = (0, 0, 0)
    assert output == expected_output


if __name__ == "__main__":
    test_second()
    test_minute()
    test_hour()
    test_zero()
    print("All tests passed!")
