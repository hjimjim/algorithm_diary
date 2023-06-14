class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        very simple approach 
        1. merge two lists
        2. sort it

        Runtime : 50ms, faster than 63.54%
        """
        nums1[m:] = nums2
        nums1.sort()