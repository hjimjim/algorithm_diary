class Solution:
    """
        Top Interview 150 (Array/ Easy)
        26. Remove Duplicates from Sorted Array
        link : https://leetcode.com/problems/remove-duplicates-from-sorted-array
        Date : Jun 14, 2023
        
        Runtime : 76ms, faster than 99.47%
        very simple approach 
        1. track index so that nums[:track] doesn't have any duplicated element
        2. during interating given list, when new element shows up 
            set new element to nums[track+1]
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        track = 0
        for i in range(len(nums)):
            if nums[i] != nums[track] :
                track += 1
                nums[track] = nums[i]
        
        return track + 1