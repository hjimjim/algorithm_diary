from typing import List

class Solution:
    """
        Top Interview 150 (TwoPointers/ Medium)
        15. 3Sum
        link : https://leetcode.com/problems/3sum/
        Date : Jun 29, 2023
        
        Runtime : 2850 ms, faster than 25.10%
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        for pivot in range(len(nums)-2):
            left = pivot + 1
            right = len(nums) - 1
            while left < right:
                temp = nums[pivot] + nums[left]  + nums[right]
                if temp == 0:
                    res.append((nums[pivot], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif temp < 0: left += 1
                else: right -= 1
            
        return set(res)
        
        
        
        