from typing import List
from collections import Counter

class Solution:
    """
        Top Interview 150 (Hashmap/ Eash)
        383. Ransom Note
        link : https://leetcode.com/problems/ransom-note/
        Date : Jun 27, 2023
        
        Runtime : 68ms, faster than 73.25%
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = Counter(magazine)
        for i in ransomNote:
            if i in hmap: 
                if hmap[i] < 1:
                    return False
                hmap[i] -= 1
            else: return False
        return True