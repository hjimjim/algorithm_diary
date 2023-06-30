from typing import List

class Solution:
    """
        Top Interview 150 (TwoPointers/ Medium)
        49. Group Anagrams
        link : https://leetcode.com/problems/group-anagrams/
        Date : Jun 30, 2023
        
        Runtime : 118 ms, faster than 58.71%
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            nextWord = str(sorted(word))
            if nextWord not in res: res[nextWord] = []
            res[nextWord].append(word)
        
        return res.values()