from typing import List

class Solution:
    """
        Top Interview 150 (Array/ Easy)
        121. Best Time to Buy and Sell Stock
        link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        Date : Jun 16, 2023
        
        Runtime : 1027ms, faster than 54.13%
    """
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_total = 0
        
        while sell < len(prices):
            current = prices[sell] - prices[buy]
            if current > 0:
                max_total = max(max_total, current)
            else:
                buy = sell
            sell += 1
     
        
        return max_total