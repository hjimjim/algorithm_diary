from typing import List
class Solution:
    """
        Top Interview 150 (BinaryTree BFS/ Medium)
        77. Combinations
        link : https://leetcode.com/problems/combinations/
        Date : July 12, 2023
        
        Runtime : 371 ms, faster than 78.16%
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start, combination):
            if len(combination) == k:
                res.append(combination[:])
                return
            
            for i in range(start,n+1):
                combination.append(i)
                backtrack(i+1, combination)
                combination.pop()

        backtrack(1, [])
        return res