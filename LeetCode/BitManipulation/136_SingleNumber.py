from typing import List
class Solution:
    """
        Top Interview 150 (Bit Manipulation/ Easy)
        136. Single Number
        link: https://leetcode.com/problems/single-number/
        Date : July 20, 2023
        
        Runtime : 92 ms, faster than 99.94%
    """
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for num in nums:
            a ^= num
        
        return a