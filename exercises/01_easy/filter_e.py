"""
Filter E

Complete the function filter_e(string) that takes a string, removes all
words containing an "e" from the string, and returns the new string.

Assume that words in the string are separated by a whitespace.

Examples:
    filter_e("I swear by the moon and the stars in the sky")
        -> "I by moon and stars in sky"
    filter_e("She sells sea shells by the sea shore") -> "by"
    filter_e("1 22 333 4444 55555") -> "1 22 333 4444 55555"
    filter_e("") -> ""
"""

# I AM NOT DONE


def filter_e(string):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_simple():
    output = filter_e("I swear by the moon and the stars in the sky")
    expected_output = "I by moon and stars in sky"
    assert output == expected_output


def test_one_word_left():
    output = filter_e("She sells sea shells by the sea shore")
    expected_output = "by"
    assert output == expected_output


def test_numbers():
    output = filter_e("1 22 333 4444 55555")
    expected_output = "1 22 333 4444 55555"
    assert output == expected_output


def test_empty_string():
    output = filter_e("")
    expected_output = ""
    assert output == expected_output


if __name__ == "__main__":
    test_simple()
    test_one_word_left()
    test_numbers()
    test_empty_string()
    print("All tests passed!")
