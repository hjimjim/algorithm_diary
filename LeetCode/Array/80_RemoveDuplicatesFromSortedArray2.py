class Solution:
    """
        Top Interview 150 (Array/ Medium)
        80. Remove Duplicates from Sorted Array II
        link : https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
        Date : Jun 14, 2023
        
        Runtime : 80ms, faster than 12.01%
        very simple approach 
        1. since each unique element needs to appear at most twice, 
            compare index and index + 2
        2. when those two elements are different move to next index, 
            but if they are the same remove element that is at index+2
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        while index + 2 < len(nums):
            if nums[index] != nums[index+2]:
                index += 1
            else:
                nums.remove(nums[index+2])
        
        return len(nums)