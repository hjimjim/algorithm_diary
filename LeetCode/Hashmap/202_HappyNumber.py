class Solution:
    """
        Top Interview 150 (TwoPointers/ Easy)
        202. Happy Number
        link : https://leetcode.com/problems/happy-number/
        Date : Jun 30, 2023
        
        Runtime : 50 ms, faster than 61.22%
    """
    def isHappy(self, n: int) -> bool:
        res = n
        checkLoop = {}
        while res != 1:
            strN = str(res)
            res = 0
            for char in strN:
                res += int(char)*int(char)
            
            if res in checkLoop: return False
            checkLoop[res] = 1
        
        return True