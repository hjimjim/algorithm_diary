from typing import List

class Solution:
    """
        Top Interview 150 (BinaryTree BFS/ Medium)
        39. Combination Sum
        link : https://leetcode.com/problems/combination-sum/
        Date : July 12, 2023
        
        Runtime : 42 ms, faster than 98.61%
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def buildCombi(candidates, new_target, sus):
            if new_target == 0:
                res.append(sus)
                return
            for i in range(len(candidates)):
                if candidates[i] > new_target:
                    continue
                buildCombi(candidates[i:],new_target-candidates[i],sus+[candidates[i]])
        buildCombi(candidates,target,[])
        return res

    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res=[]
    #     def buildCombi(candidates,target,sus):
    #         if target==0:
    #             # 여기
    #             res.append(sus[:])
    #             return
    #         for i in range(len(candidates)):
    #             if candidates[i]>target:
    #                 continue
    #             # 여기
    #             sus.append(candidates[i])
    #             buildCombi(candidates[i:],target-candidates[i])
    #             sus.pop()
    #     buildCombi(candidates,target,[])
    #     return out


    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    #     res = []
    #     def buildCombi(combi, new_target):
    #         if new_target == 0:
    #             new_combi = sorted(combi)
    #             if new_combi not in res:
    #                 res.append(new_combi)
    #             return 
    #         if new_target > 0:  
    #             for num in candidates:
    #                 combi.append(num)
    #                 buildCombi(combi, new_target-num)
    #                 combi.pop()
            
    #     buildCombi([], target)
    #     return res