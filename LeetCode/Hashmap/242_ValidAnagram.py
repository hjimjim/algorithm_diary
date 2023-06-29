from collections import Counter

class Solution:
    """
        Top Interview 150 (Hashmap/ Eash)
        242. Valid Anagram
        link : https://leetcode.com/problems/valid-anagram/
        Date : Jun 29, 2023
        
        Runtime : 48ms, faster than 97.17%
    """
    def isAnagram(self, s: str, t: str) -> bool:
        dic={}
        for c in s:
            if c not in dic: dic[c] = 0
            dic[c] += 1 
        
        for c in t:
            if c not in dic: return False
            dic[c] -= 1
            
        for value in dic.values():
            if value < 0 or value > 0:
                return False
        
        return True

    # easier solution
    # def isAnagram(self, s: str, t: str) -> bool:
    #     first = Counter(s)
    #     second = Counter(t)
        
    #     return True if first == second else False