class Solution:
    def climbStairs(self, n: int) -> int:
        """
            Top Interview 150 (DP/ Easy)
            70. Climbing Stairs
            link: https://leetcode.com/problems/climbing-stairs/
            Date : July 14, 2023
        
            Runtime : 45 ms, faster than 62.07%

            n = 1, ans = 1
            n = 2, ans = 2
            n = 3, ans = 3
            dp(n+2) = dp(n) + dp(n+1)
        """

        if n <= 2:
            return n

        prev1 = 1
        prev2 = 2

        for _ in range(n-2):
            curr = prev1 + prev2
            prev1, prev2 = prev2, curr
        
        return prev2