from typing import List

class Solution:
    """
        Top Interview 150 (Two Pointers/ Medium)
        167. Two Sum II - Input Array Is Sorted
        link : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
        Date : Jun 17, 2023
        
        Runtime : 154ms, faster than 11.81%
    """
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] == target:
                return [left+1, right+1]
            else:
                left += 1