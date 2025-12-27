"""
Run-Length Encoding

Complete the function encode(string) that performs run-length encoding on
the input string.

The function should scan the string and, for each sequence of identical
consecutive characters, append the character followed by the count of its
occurrences. The count can be any number >= 1.

For example, "AAABBBCCDAA" becomes "A3B3C2D1A2". "AAAAAAAAAAAA" becomes "A12".

You can assume that string will only consist of lowercase or uppercase letters
or an empty string.

Examples:
    encode("AAABBBCCDAA") -> "A3B3C2D1A2"
    encode("AAAAAAAAAAAA") -> "A12"
    encode("abcdef") -> "a1b1c1d1e1f1"
    encode("") -> ""
    encode("A") -> "A1"
"""

# I AM NOT DONE


def encode(string):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_mixed():
    assert encode("AAABBBCCDAA") == "A3B3C2D1A2"


def test_long_sequence():
    assert encode("AAAAAAAAAAAA") == "A12"


def test_no_repeats():
    assert encode("abcdef") == "a1b1c1d1e1f1"


def test_empty():
    assert encode("") == ""


def test_single():
    assert encode("A") == "A1"


if __name__ == "__main__":
    test_mixed()
    test_long_sequence()
    test_no_repeats()
    test_empty()
    test_single()
    print("All tests passed!")
