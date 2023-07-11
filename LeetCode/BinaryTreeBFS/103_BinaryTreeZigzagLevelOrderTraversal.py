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
        103. Binary Tree Zigzag Level Order Traversal
        link : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
        Date : July 11, 2023
        
        Runtime : 45 ms, faster than 80.82%
    """
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = [root]
        res = []
        check = True
        while queue:
            length = len(queue)
            sub = []

            for i in range(length):
                node = queue.pop(0)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                sub.append(node.val)

            if check: 
                res.append(sub)
                check = False
            else: 
                res.append(sub[::-1])
                check = True
        return res