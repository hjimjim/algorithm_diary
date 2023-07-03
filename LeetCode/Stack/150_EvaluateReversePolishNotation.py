from typing import List

class Solution:
    """
        Top Interview 150 (Stack/ Medium)
        150. Evaluate Reverse Polish Notation
        link : https://leetcode.com/problems/evaluate-reverse-polish-notation/
        Date : July 3, 2023
        
        Runtime : 71 ms, faster than 98.84%
    """
    def evalRPN(self, tokens: List[str]) -> int:
        cal = "+-*/"
        result = []
        for token in tokens:
            if token in cal:
                n1 = result.pop()
                n2 = result.pop()
                if token == "+": result.append(n2+n1)
                elif token == "-": result.append(n2-n1)
                elif token == "*": result.append(n2*n1)
                elif token == "/": result.append(int(n2/n1))
            else:
                result.append(int(token))
        return result.pop()