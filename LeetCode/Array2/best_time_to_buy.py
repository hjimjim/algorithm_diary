from typing import List

class Solution:
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
    """
    def calculate(self, prices: List[int], s) -> int :
        ma = 0

        for i in range(s, len(prices)) :
            maxProfit = 0
            for j in range(i+1, len(prices)) :
                if prices[i] < prices[j] :
                    profit = self.calculate(prices, j+1) + prices[j] - prices[i]
                    if maxProfit < profit :
                        maxProfit = profit
            if maxProfit > ma :
                ma = maxProfit 
        return ma

    def maxProfit(self, prices: List[int]) -> int:
        return self.calculate(prices, 0)
    """

prices = [7,1,5,3,6,4]
result = Solution()
length = result.maxProfit(prices)

print(length)

