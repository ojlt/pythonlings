"""
Run-Length Decoding

Complete the function decode(string) that performs run-length decoding on
the input string, which is assumed to be a valid encoding from run-length
encoding.

The function should parse the string, which contains a character followed by
a number. It should return the decoded string.

For example, "A3B3C2D1A2" becomes "AAABBBCCDAA". "A12" becomes "AAAAAAAAAAAA".

You can assume the input string is always valid.

Examples:
    decode("A3B3C2D1A2") -> "AAABBBCCDAA"
    decode("A12") -> "AAAAAAAAAAAA"
    decode("a1b1c1d1e1f1") -> "abcdef"
    decode("") -> ""
    decode("A1") -> "A"
"""

# I AM NOT DONE


def decode(string):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_mixed():
    assert decode("A3B3C2D1A2") == "AAABBBCCDAA"


def test_long_sequence():
    assert decode("A12") == "AAAAAAAAAAAA"


def test_no_repeats():
    assert decode("a1b1c1d1e1f1") == "abcdef"


def test_empty():
    assert decode("") == ""


def test_single():
    assert decode("A1") == "A"


if __name__ == "__main__":
    test_mixed()
    test_long_sequence()
    test_no_repeats()
    test_empty()
    test_single()
    print("All tests passed!")
