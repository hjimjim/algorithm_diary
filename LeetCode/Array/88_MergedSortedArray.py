class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Top Interview 150 (Array/ Easy)
        Date : Jun 14, 2023
        
        Runtime : 50ms, faster than 63.54%
        very simple approach 
        1. merge two lists
        2. sort it
        """
        nums1[m:] = nums2
        nums1.sort()