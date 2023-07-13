from typing import List

class Solution:
    """
        Top Interview 150 (BinaryTree BFS/ Medium)
        22. Generate Parentheses
        link : https://leetcode.com/problems/generate-parentheses/
        Date : July 13, 2023
        
        Runtime : 47 ms, faster than 78.44%
    """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def buildParenthesis(paren, open_count, close_count):
            if len(paren) == n*2:
                res.append(paren)
        
            if open_count < n:
                buildParenthesis(paren + "(", open_count+1, close_count)
            if close_count < open_count:
                buildParenthesis(paren + ")", open_count, close_count+1)
        
        buildParenthesis("", 0, 0)
        return res