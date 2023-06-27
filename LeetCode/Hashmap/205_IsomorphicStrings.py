from typing import List
from collections import Counter

class Solution:
    """
        Top Interview 150 (Hashmap/ Eash)
        205. Isomorphic Strings
        link : https://leetcode.com/problems/isomorphic-strings/
        Date : Jun 27, 2023
        
        Runtime : 59ms, faster than 50.98%
    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmapS = {}
        hmapT = {}
        
        for idx in range(len(s)):
            letter = s[idx]
            if letter not in hmapS: hmapS[letter] = []
            hmapS[letter].append(idx)
            
            letter2 = t[idx]
            if letter2 not in hmapT: hmapT[letter2] = []
            hmapT[letter2].append(idx)
        

        if tuple(hmapS.values()) == tuple(hmapT.values()):
            return True
        else:
            return False