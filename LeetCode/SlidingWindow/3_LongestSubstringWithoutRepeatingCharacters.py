class Solution:
    """
        Top Interview 150 (Sliding Window/ Medium)
        3. Longest Substring Without Repeating Characters
        link : https://leetcode.com/problems/longest-substring-without-repeating-characters
        Date : Jun 16, 2023
        
        Runtime : 55ms, faster than 97.58%
        1. list name lst, keeps track of longest substring
        2. iterate given string s
            if new character c is already in lst --> get index of it and update lst
            check length of the lst and if it is the longest substring update max
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        max = 0
        for c in s:
            if c in lst:
                idx = lst.index(c)
                lst = lst[idx+1:]
            lst.append(c)
            if max < len(lst):
                max = len(lst)
        return max