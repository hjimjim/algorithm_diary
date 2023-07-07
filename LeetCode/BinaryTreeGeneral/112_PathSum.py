from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Top Interview 150 (BinaryTree/ Easy)
        112. Path Sum
        link : https://leetcode.com/problems/path-sum/
        Date : July 7, 2023

        Runtime : 55 ms, faster than 78.55%
    """
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sum(head, res):
            if not head: return False
            res += head.val
            if not head.left and not head.right:
                return targetSum == res
            
            return sum(head.left, res) or sum(head.right, res)
        
        return sum(root, 0)
    
    # Runtime : 55 ms, faster than 78.55%
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if not root: 
    #         return False
    #     result = []
    #     def sum(head, res):
    #         if not head.left and not head.right:
    #             res += head.val
    #             result.append(res)
            
    #         if not head.left and head.right:
    #             sum(head.right, res + head.val)
    #         elif not head.right and head.left:
    #             sum(head.left, res + head.val)
    #         elif head.left and head.right:
    #             sum(head.left, res + head.val)
    #             sum(head.right, res + head.val)
        
    #     sum(root, 0)
    #     return True if targetSum in result else False