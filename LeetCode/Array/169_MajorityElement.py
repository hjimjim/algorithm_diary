from collections import Counter

class Solution:
    """
        Top Interview 150 (Array/ Medium)
        169. Majority Element
        link : https://leetcode.com/problems/majority-element
        Date : Jun 14, 2023
        
        Runtime : 80ms, faster than 12.01%
    """
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dic = {}
        for number in nums:
            if number not in dic: dic[number] = 0
            dic[number] += 1
        
        for number in dic:
            if dic[number] > n//2:
                return number
            
    #use Counter function instead of making dictionary myself
    def majorityElement2(self, nums: List[int]) -> int:
        n = len(nums)
        hmap = Counter(nums)
        
        for number in hmap:
            if hmap[number] > n//2:
                return number
        