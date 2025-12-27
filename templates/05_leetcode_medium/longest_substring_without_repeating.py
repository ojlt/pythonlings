"""
Longest Substring Without Repeating Characters (LeetCode #3)

Given a string s, find the length of the longest substring without
repeating characters.

Examples:
    length_of_longest_substring("abcabcbb") -> 3
        # The answer is "abc", with length 3
    length_of_longest_substring("bbbbb") -> 1
        # The answer is "b", with length 1
    length_of_longest_substring("pwwkew") -> 3
        # The answer is "wke", with length 3
"""

# I AM NOT DONE


def length_of_longest_substring(s):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert length_of_longest_substring("abcabcbb") == 3


def test_example2():
    assert length_of_longest_substring("bbbbb") == 1


def test_example3():
    assert length_of_longest_substring("pwwkew") == 3


def test_empty():
    assert length_of_longest_substring("") == 0


def test_single():
    assert length_of_longest_substring("a") == 1


def test_all_unique():
    assert length_of_longest_substring("abcdef") == 6


def test_spaces():
    assert length_of_longest_substring("a b c") == 3


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_example3()
    test_empty()
    test_single()
    test_all_unique()
    test_spaces()
    print("All tests passed!")
