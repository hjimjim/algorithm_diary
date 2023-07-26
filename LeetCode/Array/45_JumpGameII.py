from typing import List
class Solution:
    """
        Top Interview 150 (Array/ Medium)
        45. Jump Game II
        link: https://leetcode.com/problems/jump-game-ii/
        Date : July 26, 2023
        
        Runtime : 131 ms, faster than 91.92%
    """
    def jump(self, nums: List[int]) -> int:
        max_jump = 0
        end = 0
        ans = 0

        for i in range(len(nums)-1):
            max_jump = max(max_jump, i + nums[i])
            
            if max_jump >= len(nums) - 1:
                ans += 1
                break
            
            if i == end:
                ans += 1
                end = max_jump
        
        return ans