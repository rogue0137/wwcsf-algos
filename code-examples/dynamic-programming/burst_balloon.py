"""Burst Balloon

Try bursting every available balloon.
Imagine there are only three balloons remaining: left, i, right. At this state,
    1) we have already burst balloon from left to i --> remaining left
    2) we haven't touch i
    3) we have already burst balloon from i to right --> remaining right

If we go ahead and burst balloon i,
    - we'll collect nums[i] * nums[left] * nums[right] coins as specified in the problem statement
    - we'll also collect coins from bursting left to i, since we've burst them previously --> see 1)
    - plus coins from bursting i to right --> see 2)
"""

import functools


def get_max_coins(nums):
    # As given by the question.
    # You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
    nums = [1] + nums + [1]

    @functools.lru_cache(None)
    def burst(left, right):
        max_coins = 0
        for i in range(left + 1, right):
            if right - left <= 1:  # no balloon in between left and right
                return 0
            max_coins = max(max_coins, nums[left] * nums[i] * nums[right] + burst(left, i) + burst(i, right))
        return max_coins

    return burst(0, len(nums) - 1)


def get_max_coins_bottom_up(nums):
    """How to turn the recursive solution the other way around?
    By creating our own cache/table.

    """
    nums = [1] + nums + [1]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    # We want the equivalent of burst(0, len(nums) - 1), so our final result will be in dp[0][len(nums) - 1]
    # Thus, we start left from n - 1 in order to get to 0 in the end.
    for left in range(n - 1, -1, -1):
        # right starts from 2 away from left since we need at least 1 balloon in the middle of left and right
        for right in range(left + 2, n):
            for i in range(left + 1, right):  # The middle balloon between left and right.
                dp[left][right] = max(dp[left][right], nums[i] * nums[left] * nums[right] + dp[left][i] + dp[i][right])
    return dp[0][len(nums) - 1]


if __name__ == "__main__":
    print(get_max_coins([3, 1, 5, 8]))
    print(get_max_coins([1]))
    print(get_max_coins([6, 3, 2, 4]))
    print(get_max_coins([8, 8, 8, 8]))
    print(get_max_coins_bottom_up([3, 1, 5, 8]))
    print(get_max_coins_bottom_up([1]))
    print(get_max_coins_bottom_up([6, 3, 2, 4]))
    print(get_max_coins_bottom_up([8, 8, 8, 8]))
