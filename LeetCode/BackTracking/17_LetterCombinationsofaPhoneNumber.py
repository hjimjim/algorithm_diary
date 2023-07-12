class Solution:
    """
        Top Interview 150 (BinaryTree BFS/ Medium)
        17. Letter Combinations of a Phone Number
        link : https://leetcode.com/problems/letter-combinations-of-a-phone-number/
        Date : July 12, 2023
        
        Runtime : 46 ms, faster than 62.69%
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: 
            return []
        
        res = []
        phone_digits = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtracking(combination, next):
            if not next:
                res.append(combination)
                return 
            
            for letter in phone_digits[next[0]]:
                backtracking(combination+letter, next[1:])
            
        backtracking("", digits)
        return res