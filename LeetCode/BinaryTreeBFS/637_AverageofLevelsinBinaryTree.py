from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Top Interview 150 (BinaryTree BFS/ Easy)
        637. Average of Levels in Binary Tree
        link : https://leetcode.com/problems/average-of-levels-in-binary-tree/
        Date : July 11, 2023
        
        Runtime : 59 ms, faster than 89.4%
    """
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        need = [root]
        res = list()
        while need:
            length = len(need)
            sum_depth = 0

            for i in range(length):
                node = need.pop(0)
                sum_depth += node.val
                if node.left: need.append(node.left)
                if node.right: need.append(node.right)
            
            res.append(sum_depth/length)
            
        return res
