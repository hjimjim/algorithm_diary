from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        tmp=[None] * k
        for j in range(1,k+1) :
            tmp[k-j] = nums[-j]
      
        for i in range(len(nums)-1, 0, -1) :
            nums[i] = nums[i - k]
        for j in range(0,k) :
            nums[j] = tmp[j]
        print(nums)


nums = [1,2]
result = Solution()
length = result.rotate(nums, 3)

