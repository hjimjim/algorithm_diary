from typing import List

class Solution:
    """
        Top Interview 150 (Array/ Medium)
        238. Product of Array Except Self
        link: https://leetcode.com/problems/product-of-array-except-self/
        Date : July 31, 2023
        
        Runtime : 190 ms, faster than 99.09% 
        다른 솔루션들을 살펴 보았을때 postfix, prefix를 구하는 방법으로 정형화되어 있는듯 보임
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total = 1
        zero_index = []
        res = []
        for i,num in enumerate(nums):
            if num == 0: zero_index.append(i)
            else: total *= num

        if len(zero_index) >= 2:
            return [0] * len(nums)

        for i in range(len(nums)):
            if i in zero_index: res.append(int(total))
            else:
                if len(zero_index) >= 1: res.append(0)
                else: res.append(int(total/nums[i]))

        return res