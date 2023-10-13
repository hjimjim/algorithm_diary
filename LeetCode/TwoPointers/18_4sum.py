from typing import List

class Solution:
    """
        Top Interview 150 (TwoPointers/ Medium)
        15. 4Sum
        link : https://leetcode.com/problems/4sum/
        Date : Oct 13, 2023
        
        Runtime : 885 ms, faster than 36.62%
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        for ans in range(len(nums) - 3):
            result = target - nums[ans]

            for pivot in range(ans + 1, len(nums) - 2):
                left = pivot + 1
                right = len(nums) - 1

                while left < right :
                    temp = nums[pivot] + nums[left] + nums[right]
                    if temp == result: 
                        res.append((nums[ans], nums[pivot], nums[left], nums[right]))
                        left += 1
                        right -= 1
                    elif temp > result: right -= 1
                    else: left += 1
        return set(res)
        
        
        
        