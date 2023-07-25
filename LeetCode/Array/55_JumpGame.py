from typing import List
class Solution:
    """
        Top Interview 150 (Array/ Medium)
        55. Jump Game
        link: https://leetcode.com/problems/jump-game/
        Date : July 25, 2023
        
        Runtime : 463 ms, faster than 75.52%
        used greedy algorithm
    """
    def canJump(self, nums: List[int]) -> bool:
        lastIndex = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= lastIndex:
                lastIndex = i
        
        return lastIndex == 0