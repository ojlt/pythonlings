"""
Count Repeats

Complete the function count_repeats(word) to check whether every letter in
the given word occurs the same number of times. For example, "byebye" has all
three characters occurring exactly twice.

Your function should return an int indicating the number of repeats if all
letters occur the same number of times, or 0 if not all characters repeat
the same number of times.

Your function should be case-sensitive, so "A" and "a" are treated as
different characters.

You can assume that word will be a str made up of digits and lowercase letters.

Examples:
    count_repeats("byebye") -> 2  (b, y and e all appear twice)
    count_repeats("abba") -> 2
    count_repeats("aabbcacbabcc") -> 4
    count_repeats("123456789") -> 1  (all characters appear exactly once)
    count_repeats("cake") -> 1
    count_repeats("yaba1yaba1") -> 0  (a appears 4 times, others appear twice)
    count_repeats("dingdong") -> 0  (i and o appear once, others appear twice)
"""

# I AM NOT DONE


def count_repeats(word):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test():
    answer = count_repeats("byebye")
    assert answer == 2

    answer = count_repeats("cake")
    assert answer == 1

    answer = count_repeats("aabbcacbabcc")
    assert answer == 4

    answer = count_repeats("12345678")
    assert answer == 1

    answer = count_repeats("yaba1yaba1")
    assert answer == 0

    answer = count_repeats("dingdong")
    assert answer == 0


if __name__ == "__main__":
    test()
    print("All tests passed!")
