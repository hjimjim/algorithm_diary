class Solution:
    """
        Top Interview 150 (Array/ Medium)
        28. Find the Index of the First Occurrence in a String
        link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
        Date : July 28, 2023
        
        Runtime : 32 ms, faster than 98.99% 
    """
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        return -1