# 2020.05.15 after work
# https://leetcode.com/problems/single-number/
from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # 88ms 16.4MB
        return 2*sum(set(nums)) - sum(nums)
        """
        # 92ms 16.5MB
        a = 0
        for num in nums:
            a ^= num
        return a
        
        # Time Limit
        for i,num in enumerate(nums):
            nums[i] = None
            if num not in nums:
                return num
            else:
                nums[nums.index(num)] = None
        """



result = Solution()
a = [4,1,2,1,2]
print(result.singleNumber(a))