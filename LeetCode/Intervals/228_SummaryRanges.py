from typing import List
class Solution:
    """
        Top Interview 150 (Intervals/ Easy)
        228. Summary Ranges
        link : https://leetcode.com/problems/summary-ranges/
        Date : July 19, 2023
        
        Runtime : 56ms, faster than 5.72%
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start = nums[0]
        end = nums[0]
        res = []
        for idx in range(1,len(nums)):
            if nums[idx] - nums[idx-1] == 1:
                end = nums[idx]
            else:
                if start == end:
                    res.append(str(start))
                else:
                    ans = str(start) + "->" + str(end)
                    res.append(ans)
                start = nums[idx]
                end = nums[idx]
        
        if start == end:
            res.append(str(start))
        else:
            ans = str(start) + "->" + str(end)
            res.append(ans)
            
        return res