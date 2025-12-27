"""
Coin Change (LeetCode #322)

You are given an integer array coins representing coins of different
denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

You may assume that you have an infinite number of each kind of coin.

Examples:
    coin_change([1, 2, 5], 11) -> 3
        # 11 = 5 + 5 + 1
    coin_change([2], 3) -> -1
        # Cannot make 3 with only 2s
    coin_change([1], 0) -> 0
        # No coins needed for amount 0
"""

# I AM NOT DONE


def coin_change(coins, amount):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert coin_change([1, 2, 5], 11) == 3


def test_example2():
    assert coin_change([2], 3) == -1


def test_zero_amount():
    assert coin_change([1], 0) == 0


def test_single_coin():
    assert coin_change([1], 5) == 5


def test_exact_match():
    assert coin_change([1, 5, 10], 10) == 1


def test_greedy_fails():
    # Greedy would pick 6+1+1+1 = 4 coins, but optimal is 4+4+1 = 3 coins
    assert coin_change([1, 4, 6], 9) == 3


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_zero_amount()
    test_single_coin()
    test_exact_match()
    test_greedy_fails()
    print("All tests passed!")
