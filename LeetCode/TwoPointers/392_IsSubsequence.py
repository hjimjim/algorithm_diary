class Solution:
    """
        Top Interview 150 (Two Pointers/ Easy)
        392. Is Subsequence
        link : https://leetcode.com/problems/is-subsequence/
        Date : Jun 16, 2023
        
        Runtime : 58ms, faster than 8.56%
    """
    def isSubsequence(self, s: str, t: str) -> bool:
        subsequenceIdx = 0 
        originalIdx = 0
        
        while originalIdx < len(t) and subsequenceIdx < len(s):
            if s[subsequenceIdx] == t[originalIdx]:
                subsequenceIdx += 1
                originalIdx += 1
            else:
                originalIdx += 1
                
        return subsequenceIdx == len(s)