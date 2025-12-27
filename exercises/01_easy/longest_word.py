"""
Longest Word

Complete the function longest_word(words) that returns the longest word in
words and also the length of this longest word.

words will always be a list of str.

The function should return a tuple, where the first item in the tuple is the
longest word, and the second item is the length of this word.

If more than one word have the same highest length, return the one that occurs
first in the list.

You may assume that there is always at least one item in the list.

Examples:
    longest_word(["I", "love", "Python", "programming", "the", "most"])
        -> ("programming", 11)
    longest_word(["Caught", "in", "a", "landslide", "no", "escape", "from", "reality"])
        -> ("landslide", 9)
    longest_word(["Llanfairpwllgwyngyll"]) -> ("Llanfairpwllgwyngyll", 20)
    longest_word(["laugh", "reach", "go", "climb", "jump"]) -> ("laugh", 5)
    longest_word(["", "", "", "", ""]) -> ("", 0)
"""

# I AM NOT DONE


def longest_word(words):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_simple():
    words = ["I", "love", "Python", "programming", "the", "most"]
    output = longest_word(words)
    expected_output = ("programming", 11)
    assert output == expected_output


def test_queen():
    words = ["Caught", "in", "a", "landslide", "no", "escape", "from", "reality"]
    output = longest_word(words)
    expected_output = ("landslide", 9)
    assert output == expected_output


def test_single():
    words = ["Llanfairpwllgwyngyll"]
    output = longest_word(words)
    expected_output = ("Llanfairpwllgwyngyll", 20)
    assert output == expected_output


def test_same_max_length():
    words = ["laugh", "reach", "go", "climb", "jump"]
    output = longest_word(words)
    expected_output = ("laugh", 5)
    assert output == expected_output


def test_empty_strings():
    words = ["", "", "", "", ""]
    output = longest_word(words)
    expected_output = ("", 0)
    assert output == expected_output


if __name__ == "__main__":
    test_simple()
    test_queen()
    test_single()
    test_same_max_length()
    test_empty_strings()
    print("All tests passed!")
