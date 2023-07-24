from typing import List
class Solution:
    """
        Top Interview 150 (DP/ Medium)
        322. Coin Change
        link: https://leetcode.com/problems/coin-change/
        Date : July 24, 2023
        
        Runtime : 1376 ms, faster than 53.98%
        dp[num] = min(dp[array], dp[array-coin]+1)
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]*(amount+1)
        dp[0] = 0

        for array in range(1, amount+1):
            for coin in coins:
                if array-coin >=0:
                    dp[array] = min(dp[array], dp[array-coin] +1)
        return dp[amount] if dp[amount] != amount+1 else -1