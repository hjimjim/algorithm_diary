class Solution:
    """
        Top Interview 150 (Bit Manipulation/ Easy)
        191. Number of 1 Bits
        link: https://leetcode.com/problems/number-of-1-bits/
        Date : July 15, 2023
        
        Runtime : 32 ms, faster than 99.35%
    """
    def hammingWeight(self, n: int) -> int:
        str_n = str(bin(n))
        ans = 0
        for val in str_n[2:]:
            ans += int(val)
        
        return ans