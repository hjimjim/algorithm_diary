class Solution:
    """
        Top Interview 150 (Multidimensional DP/ Medium)
        5. Longest Palindromic Substring
        link: https://leetcode.com/problems/longest-palindromic-substring/
        Date : July 2, 2023
        
        Runtime : 5943 ms, faster than 14.068%
    """
    def longestPalindrome(self, s: str) -> str:
        asw = ""
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s),i,-1):  # j = end, O = n^2
                if len(asw) >= j-i:
                    break
                if s[i:j] == s[i:j][::-1]:
                    asw = s[i:j]
                    break
        return asw
