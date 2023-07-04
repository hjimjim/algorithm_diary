# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Top Interview 150 (BinaryTree/ Easy)
        104. Maximum Depth of Binary Tree
        link : https://leetcode.com/problems/maximum-depth-of-binary-tree/
        Date : July 4, 2023
        
        Runtime : 44 ms, faster than 97.97%
    """
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        
        if root.left != None and root.right != None:
            return max(self.maxDepth(root.right), self.maxDepth(root.left))+1
        elif root.right != None:
            return self.maxDepth(root.right) + 1
        elif root.left != None:
            return self.maxDepth(root.left) + 1