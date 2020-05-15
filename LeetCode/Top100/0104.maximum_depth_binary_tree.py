# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 2020.05.15 after work
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        count = 0
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