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
        226. Invert Binary Tree
        link : https://leetcode.com/problems/invert-binary-tree/
        Date : July 5, 2023
        
        Runtime : 35 ms, faster than 98.29%
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        if not root.left and not root.right: return root
        else:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        