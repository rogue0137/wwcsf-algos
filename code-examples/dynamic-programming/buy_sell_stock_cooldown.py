"""Buy and Sell Stock with Cooldown

Define two states to keep track of max profit so far:
    - buy, max profit so far, last transaction is buy
    - sell, max profit so far, last transaction is sell

buy[i] means we buy today, the max profit is buy[i].
sell[i] means we sell today, the max profit is sell[i].

Thus,
    - buy[i] = max(sell[i - 2] - price, buy[i - 1])
      -- sell the day before since we can't sell yesterday,
      -- or do nothing (carry over the profit from yesterday's buy: buy[i - 1])
    - sell[i] = max(buy[i - 1] + price, sell[i - 1])
      -- in order to sell today, we can buy yesterday so buy[i - 1] is allowed,
      -- or do nothing (sell[i - 1])
"""


def max_profit(prices):
    """Sample O(n) time O(n) space implementation.

    Returns:
        int: The maximum profit that we can make.
    """
    n = len(prices) + 2  # 2 is just an offset to help with index lookup.
    buy = [float('-inf')] * n
    sell = [0] * n  # Initialise at 0 assuming that we don't sell at loss.
    for i in range(2, n):
        buy[i] = max(sell[i - 2] - prices[i - 2], buy[i - 1])
        sell[i] = max(buy[i - 1] + prices[i - 2], sell[i - 1])
    return sell[n - 1]


def max_profit_1d(prices):
    """Improves the space to O(1).

    Returns:
        int: The maximum profit that we can make.
    """
    n = len(prices)
    buy = float('-inf')  # Replaces buy[i - 1]
    sell = 0  # Replaces sell[i - 1]
    prev_sell = 0  # Replaces sell[i - 2]
    for i, price in enumerate(prices):
        buy, sell, prev_sell = max(prev_sell - price, buy), max(buy + price, sell), sell
    return sell


if __name__ == "__main__":
    print(max_profit([1, 2, 3, 0, 2]))
    print(max_profit([5, 5, 5, 5, 5, 10]))
    print(max_profit([1]))  # Should be 0 as we can't sell on the same day.
    print(max_profit([10, 9, 8, 7]))  # We never sell at loss.
    print(max_profit([7, 7, 7, 7, 7, 7, 7]))  # Keep holding the stocks if the price never changes.
