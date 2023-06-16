class Solution:
     """
        Top Interview 150 (Two Pointers/ Easy)
        125. Valid Palindrome
        link : https://leetcode.com/problems/valid-palindrome
        Date : Jun 16, 2023
        
        Runtime : 62ms, faster than 58.94%
    """
     def isPalindrome(self, s: str) -> bool:

        s = "".join(filter(str.isalnum, s)).lower()
        left = 0
        right = len(s) -1
        
        while left < right:
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True