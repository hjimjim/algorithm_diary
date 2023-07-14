from typing import List
class Solution:
    """
        Top Interview 150 (BinaryTree BFS/ Medium)
        46. Permutations
        link : https://leetcode.com/problems/permutations/
        Date : July 12, 2023
        
        Runtime : 42 ms, faster than 98.61%
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def permutation(permu):
            if len(permu) == len(nums):
                res.append(permu)
                return 
            for i in nums:
                if i not in permu:
                    permutation(permu + [i])
        
        permutation([])
        return res

        # def permutation(permu):
        #     if len(permu) == len(nums):
        #         res.append(permu[:])
        #         return 
        #     for i in nums:
        #         if i not in permu:
        #             permu.append(i)
        #             permutation(permu)
        #             permu.pop()
        
        # permutation([])
        # return res