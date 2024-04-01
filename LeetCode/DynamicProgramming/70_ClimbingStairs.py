class Solution:
    def climbStairs(self, n: int) -> int:
        """
            Top Interview 150 (DP/ Easy)
            70. Climbing Stairs
            link: https://leetcode.com/problems/climbing-stairs/
            Date : Apr 1, 2024
    
            n = 1, ans = 1
            n = 2, ans = 2
            n = 3, ans = 3
            dp(n+2) = dp(n) + dp(n+1)
        """

        memo = [1,2]
        
        for i in range(2, n):
            memo.append(memo[i-1] + memo[i-2])
        
        return memo[n-1]