class Solution:
    def longestPalindrome(self, s: str) -> str:
        asw = ""
        for i in range(len(s)):  # i = start, O = n
            for j in range(len(s),i,-1):  # j = end, O = n^2
                if len(asw) >= j-i:
                    break
                if s[i:j] == s[i:j][::-1]:
                    asw = s[i:j]
                    break
        return asw



result = Solution()
print(result.longestPalindrome("baabad"))