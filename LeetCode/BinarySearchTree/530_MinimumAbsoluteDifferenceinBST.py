from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Top Interview 150 (BinarySearchTree/ Easy)
        530. Minimum Absolute Difference in BST
        link : https://leetcode.com/problems/minimum-absolute-difference-in-bst/
        Date : July 8, 2023
        
        Runtime : 78 ms, faster than 30.34%
    """
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float('inf')
        def getMaxLeft(subTree):
            #get max of left child
            return getMaxLeft(subTree.right) if subTree.right else subTree.val
        def getMinRight(subTree):
            #get min of right child 
            return getMinRight(subTree.left) if subTree.left else subTree.val

        def getMin(res, subTree):
            if subTree.right:
                res = getMin(min(getMinRight(subTree.right) - subTree.val, res), subTree.right)
            if subTree.left:
                res = getMin(min(subTree.val - getMaxLeft(subTree.left), res), subTree.left)
            return res
        return getMin(res, root)