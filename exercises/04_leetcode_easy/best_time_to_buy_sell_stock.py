"""
Best Time to Buy and Sell Stock (LeetCode #121)

You are given an array prices where prices[i] is the price of a given stock
on the ith day.

You want to maximize your profit by choosing a single day to buy one stock
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you
cannot achieve any profit, return 0.

Examples:
    max_profit([7, 1, 5, 3, 6, 4]) -> 5
        # Buy on day 2 (price=1), sell on day 5 (price=6), profit = 6-1 = 5
    max_profit([7, 6, 4, 3, 1]) -> 0
        # No profit possible, prices only decrease
"""

# I AM NOT DONE


def max_profit(prices):
    pass


# ============================================================================
# Tests - Do not modify below this line
# ============================================================================
def test_example1():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5


def test_example2():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_single_day():
    assert max_profit([5]) == 0


def test_two_days_profit():
    assert max_profit([1, 5]) == 4


def test_two_days_loss():
    assert max_profit([5, 1]) == 0


def test_constant_price():
    assert max_profit([3, 3, 3, 3]) == 0


def test_buy_at_end():
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4


if __name__ == "__main__":
    test_example1()
    test_example2()
    test_single_day()
    test_two_days_profit()
    test_two_days_loss()
    test_constant_price()
    test_buy_at_end()
    print("All tests passed!")
