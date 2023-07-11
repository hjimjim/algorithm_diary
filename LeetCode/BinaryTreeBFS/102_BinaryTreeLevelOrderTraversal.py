from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Top Interview 150 (BinaryTree BFS/ Medium)
        102. Binary Tree Level Order Traversal
        link : https://leetcode.com/problems/binary-tree-level-order-traversal/
        Date : July 11, 2023
        
        Runtime : 52 ms, faster than 78.54%
    """

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        need = list([root])
        res = list()

        while need:
            length = len(need)
            same_depth_val = list()
            for i in range(length):
                node = need.pop(0)
                if node.left: 
                    need.append(node.left)
                if node.right: 
                    need.append(node.right)
                same_depth_val.append(node.val)
            
            res.append(same_depth_val)
        
        return res
    
    # small change makes big difference
    # def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    #     if not root: return []
    #     need = list([root])
    #     res = list([[root.val]])

    #     while need:
    #         length = len(need)
    #         same_depth_val = list()
    #         for i in range(length):
    #             node = need.pop(0)
    #             if node.left: 
    #                 same_depth_val.append(node.left.val)
    #                 need.append(node.left)
    #             if node.right: 
    #                 same_depth_val.append(node.right.val)
    #                 need.append(node.right)
            
    #         if same_depth_val:
    #             res.append(same_depth_val)
        
    #     return res

    