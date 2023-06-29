from typing import List

class Solution:
    """
        Top Interview 150 (Hashmap/ Easy)
        1. Two Sum
        link : https://leetcode.com/problems/two-sum/
        Date : Jun 29, 2023
        
        Runtime : 604 ms, faster than 39.21%
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            if target - nums[i] in nums[i+1:]:
                return [i, nums.index(target-nums[i], i+1)]
            
    
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_nums = sorted(nums)
        size = len(nums)
        i = 0
        j = size - i - 1
        while i < j:
            temp = new_nums[i] + new_nums[j]
            if target == temp:
                if new_nums[i] == new_nums[j]:
                    first = nums.index(new_nums[i])
                    temp = [nums.index(new_nums[i]), nums.index(new_nums[j],first + 1)]
                else:
                    temp = [nums.index(new_nums[i]), nums.index(new_nums[j])]                
                return temp
            elif target < temp:
                j = j - 1
            elif target > temp:
                i = i + 1
    """
