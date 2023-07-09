class Solution:
    """
        Top Interview 150 (Math/ Easy)
        9. Palindrome Number
        link : https://leetcode.com/problems/palindrome-number/
        Date : July 9, 2023
        
        Runtime : 77 ms, faster than 54.37%
    """
    def isPalindrome(self, x: int) -> bool:
        string_x = str(x)

        if string_x == string_x[::-1]:
            return True
        else:
            return False