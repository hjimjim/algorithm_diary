class Solution:
    """
        Top Interview 150 (Hashmap/ Eash)
        290. Word Pattern
        link : https://leetcode.com/problems/word-pattern/
        Date : Jun 27, 2023
        
        Runtime : 51ms, faster than 26.16%
    """
    def wordPattern(self, pattern: str, s: str) -> bool:
        patternS = s.split(" ")
        hmap = {}
        hmapS = {}
        for idx in range(len(pattern)):
            if pattern[idx] not in hmap: hmap[pattern[idx]] = []
            hmap[pattern[idx]].append(idx)
        for idx in range(len(patternS)):
            if patternS[idx] not in hmapS: hmapS[patternS[idx]] = []
            hmapS[patternS[idx]].append(idx)
            

        if tuple(hmap.values()) == tuple(hmapS.values()):
            return True
        else: return False
            