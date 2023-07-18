from typing import List
class Solution:
    """
        Top Interview 150 (Array/ Easy)
        14. Longest Common Prefix
        link : https://leetcode.com/problems/longest-common-prefix/
        Date : July 18, 2023
        
        Runtime : 45ms, faster than 83.91%
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)

        first = strs[0]
        last = strs[-1]

        ans = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]

        return ans


