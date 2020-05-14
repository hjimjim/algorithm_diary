from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # fourth solution -> 44m 
        dic = {}
        for i, num in enumerate(nums):
            n = target-num
            if n in dic:
                return [dic[n], i]
            dic[num] = i

      
        return None
        """ 
        # third solution -> pass not that slow (1168 ms)
        for i, num in enumerate(nums):
            if target - num in nums :
                j = nums.index(target-num)
                if j != i:
                    return [i, j]

        # second solution -> pass but slow (6296 ms)
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if num+num2 == target:
                    return [i, j]

        # first solution -> time limit exceeded
        for i, num in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num + num2 == target:
                    return [i, j]

        """
        return None

nums = [3, 3]
result = Solution()
print(result.twoSum(nums, 6))