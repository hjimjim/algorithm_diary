
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        track = 0
        for i in range(len(nums)):
            if nums[i] != nums[track] :
                track += 1
                nums[track] = nums[i]
        
        return track + 1


nums = [0,0,1,1,1,2,2] 
result = Solution()
length = result.removeDuplicates(nums)

print(nums[:length])


        