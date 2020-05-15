class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ## Second summit = 60ms
        lst = []
        max = 0
        for c in s:
            if c in lst:
                idx = lst.index(c)
                lst = lst[idx+1:]
            lst.append(c)
            if max < len(lst):
                max = len(lst)
        return max

        """
        ## First Summit 236ms
        lst = []
        count = 0
        max = 0
        for c in s:
            if c in lst:
                for i, a in enumerate(lst):
                    if a == c:
                        lst = lst[i+1:]
                        count = len(lst)
                count += 1
                lst.append(c)
            else:
                lst.append(c)
                count += 1
            if max < count:
                max = count
        return max
        
        """

result = Solution()
print(result.lengthOfLongestSubstring("pwwkew"))
            