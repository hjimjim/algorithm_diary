class Solution:
    """
        Top Interview 150 (Array/ Easy)
        13. Roman to Integer
        link : https://leetcode.com/problems/roman-to-integer/
        Date : Jun 18, 2023
        
        Runtime : 53ms, faster than 93.93%
    """
    def romanToInt(self, s: str) -> int:
        roman_dic = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000} 
        total = 0
        def recur(s, total):
            if len(s) == 0:
                return total
            temp = roman_dic[s[-1]]
            if 4 * temp < total: total -= temp
            else: total += temp
            return recur(s[:-1], total)

        return recur(s, 0)