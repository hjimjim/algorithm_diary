from typing import List

class Solution:
    """
        Top Interview 150 (TwoPointers/ Easy)
        121. Best Time to Buy and Sell Stock
        link : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
        Date : Jun 28, 2023
        
        Runtime : 1027 ms, faster than 53.62%
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
    

    """
    code that took too long
    class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_total = -10000
        for i in range(len(prices)-1):
            total = max(prices[i+1:]) - prices[i]
            if total > max_total: max_total = total
        return max_total if max_total > 0 else 0
    """