"""
Word Segmentation

Complete the function can_segment(string, word_set). This function takes a
string and a set of strings word_set.

The function should return True if string can be segmented into a space-
separated sequence of one or more words from the word_set. It should return
False otherwise. The same word in word_set may be reused multiple times.

Examples:
    can_segment("imperial", {"imperial", "college"}) -> True
    can_segment("imperialcollege", {"imperial", "college"}) -> True
    can_segment("catsanddog", {"cats", "dog", "sand", "and", "cat"}) -> True
    can_segment("catsandog", {"cats", "dog", "sand", "and", "cat"}) -> False
    can_segment("aaaaaaaa", {"a", "aa", "aaa"}) -> True
"""

# I AM NOT DONE


def can_segment(string, word_set):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_single_word():
    assert can_segment("imperial", {"imperial", "college"}) == True


def test_two_words():
    assert can_segment("imperialcollege", {"imperial", "college"}) == True


def test_multiple_words():
    assert can_segment("catsanddog", {"cats", "dog", "sand", "and", "cat"}) == True


def test_impossible():
    assert can_segment("catsandog", {"cats", "dog", "sand", "and", "cat"}) == False


def test_reuse_words():
    assert can_segment("aaaaaaaa", {"a", "aa", "aaa"}) == True


def test_empty_string():
    assert can_segment("", {"a", "b"}) == True


def test_no_match():
    assert can_segment("hello", {"world", "foo", "bar"}) == False


if __name__ == "__main__":
    test_single_word()
    test_two_words()
    test_multiple_words()
    test_impossible()
    test_reuse_words()
    test_empty_string()
    test_no_match()
    print("All tests passed!")
