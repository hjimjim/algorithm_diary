class Solution:
    """
        Top Interview 150 (Stack/ Easy)
        20. Valid Parentheses
        link : https://leetcode.com/problems/valid-parentheses/
        Date : July 1, 2023
        
        Runtime : 49 ms, faster than 45.88%
    """
    def isValid(self, s: str) -> bool:
        stack = []
        dic = { ')' : '(' , ']' : '[' , '}' : '{' }

        for check in s:
            if check in dic.values():
                stack.append(check)
            else:
                if len(stack) == 0:
                    return False
                if dic[check] != stack[-1] :
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True