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
        100. Same Tree
        link : https://leetcode.com/problems/same-tree/
        Date : July 5, 2023
        
        Runtime : 44 ms, faster than 74.38%
    """
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)