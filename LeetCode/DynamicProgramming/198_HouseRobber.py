from typing import List
class Solution:
    """
        Top Interview 150 (DP/ Medium)
        198. House Robber
        link: https://leetcode.com/problems/house-robber/
        Date : July 14, 2023
        
        Runtime : 43 ms, faster than 83.45%
    """
    
    def rob(self, nums: List[int]) -> int:
        first, second = 0, 0

        for current in nums:
            rob = max(current + first, second)
            first = second
            second = rob
        
        return rob
    
    # def rob(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     if n == 1: return nums[0]
    #     if n == 2: return max(nums[0], nums[1])


    #     rob = [0] * (n+1)
    #     rob[1] = nums[0]
    #     rob[2] = nums[1]
    #     rob[3] = nums[2] + nums[0]
    #     for i in range(4, n+1):
    #         rob[i] = max(rob[i-3],rob[i-2]) + nums[i-1]
        
    #     return max(rob[n], rob[n-1])