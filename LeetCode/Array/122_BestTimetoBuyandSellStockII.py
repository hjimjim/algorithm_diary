from typing import List

class Solution:
    """
        Top Interview 150 (Array/ Medium)
        122. Best Time to Buy and Sell Stock II
        link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
        Date : Jun 17, 2023
        
        Runtime : 60ms, faster than 99.30%
    """
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0;
        sub_profit = 0;
        if len(prices) == 0 or len(prices) == 1:
            return 0
        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                sub_profit = 0
            elif prices[i] > prices[i-1]:
                sub_profit = prices[i] - prices[i-1]
                profit += sub_profit
            elif prices[i] == prices[i-1]:
                continue
        return profit