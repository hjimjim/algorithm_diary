class Solution:
    """
        Top Interview 150 (Array/ Easy)
        27. Remove Element 
        link : https://leetcode.com/problems/remove-element/
        Date : Jun 14, 2023
        
        Runtime : 45ms, faster than 76.75%
        very simple approach 
        1. count number of element that equals to val
        2. find element index and switch places with the last element
           --> to save time spent when reordering array elements
        3. repeat 1, 2 until there is no more elements that equal to val
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        total = nums.count(val)   
        deleted = 0
        while deleted < total:
            find = nums.index(val)
            nums[find] = nums[-1]
            nums.pop()
            deleted += 1
        return len(nums)