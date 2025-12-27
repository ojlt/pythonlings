"""
Simplify Fraction

Complete the function simplify_fraction(numerator, denominator) that
simplifies a fraction numerator/denominator to its most simplified form.

The function should return a tuple (numerator, denominator).

You can assume that numerator and denominator are always positive integers.

Examples:
    simplify_fraction(4, 8) -> (1, 2)
    simplify_fraction(15, 5) -> (3, 1)
    simplify_fraction(200, 300) -> (2, 3)
    simplify_fraction(7, 9) -> (7, 9)
"""

# I AM NOT DONE


def simplify_fraction(numerator, denominator):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_simple_fraction():
    output = simplify_fraction(4, 8)
    expected_output = (1, 2)
    assert output == expected_output


def test_larger_numerator():
    output = simplify_fraction(15, 5)
    expected_output = (3, 1)
    assert output == expected_output


def test_large_factor():
    output = simplify_fraction(200, 300)
    expected_output = (2, 3)
    assert output == expected_output


def test_no_simplification():
    output = simplify_fraction(7, 9)
    expected_output = (7, 9)
    assert output == expected_output


if __name__ == "__main__":
    test_simple_fraction()
    test_larger_numerator()
    test_large_factor()
    test_no_simplification()
    print("All tests passed!")
