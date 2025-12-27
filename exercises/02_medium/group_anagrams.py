"""
Group Anagrams

Complete the function group_anagrams(words) which takes a list of strings
words. The function should group the anagrams together and return a dictionary.

An anagram is a word formed by rearranging the letters of a different word.
For example, "eat", "tea" and "ate" are anagrams of each other.

The keys of the dictionary should be the alphabetically sorted string of
characters (e.g., "aet" for "eat"). The values should be a list of the original
words from the input that are anagrams of that key. The list of words for each
key should also be sorted alphabetically in ascending order.

Examples:
    group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        -> {"aet": ["ate", "eat", "tea"], "ant": ["nat", "tan"], "abt": ["bat"]}
    group_anagrams(["listen", "silent", "enlist"])
        -> {"eilnst": ["enlist", "listen", "silent"]}
    group_anagrams(["a"]) -> {"a": ["a"]}
    group_anagrams([]) -> {}
"""

# I AM NOT DONE


def group_anagrams(words):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_multiple_groups():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = {"aet": ["ate", "eat", "tea"], "ant": ["nat", "tan"], "abt": ["bat"]}
    result = group_anagrams(words)
    assert result == expected


def test_single_group():
    words = ["listen", "silent", "enlist"]
    expected = {"eilnst": ["enlist", "listen", "silent"]}
    result = group_anagrams(words)
    assert result == expected


def test_single_word():
    words = ["a"]
    expected = {"a": ["a"]}
    result = group_anagrams(words)
    assert result == expected


def test_empty():
    words = []
    expected = {}
    result = group_anagrams(words)
    assert result == expected


if __name__ == "__main__":
    test_multiple_groups()
    test_single_group()
    test_single_word()
    test_empty()
    print("All tests passed!")
