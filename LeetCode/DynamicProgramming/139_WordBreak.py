from typing import List

class Solution:
    """
        Top Interview 150 (DP / Medium)
        139. Word Break
        link : https://leetcode.com/problems/word-break/
        Date : July 21, 2023
        
        Runtime : 42 ms, faster than 97.30%
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def isBreakable(index):
            if index == len(s):
                return True

            if index in memo: 
                return memo[index]

            for word in wordDict:
                if s.startswith(word, index) and isBreakable(index + len(word)):
                    memo[index] = True
                    return True
                    
            memo[index] = False 
            return False

        return isBreakable(0)