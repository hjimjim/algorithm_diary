from typing import List

# 2020.05.14 after work
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # third submit 208ms | 18.4MB 
        # this is not in-place, it creates a reversed copy of the list
        s[:]=s[::-1]

        """
        # second submit 212ms | 18.3MB
        s.reverse()
        # first submit 216ms | 18.2MB
        for i in range(0, len(s)//2):
            s[i], s[len(s)-1-i] = s[len(s)-1-i],s[i]
        """

result = Solution()

        
        