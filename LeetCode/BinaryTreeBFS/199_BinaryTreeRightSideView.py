from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Top Interview 150 (BinaryTree/ Easy)
        199. Binary Tree Right Side View
        link : https://leetcode.com/problems/binary-tree-right-side-view/
        Date : July 10, 2023
        
        Runtime : 32 ms, faster than 99.49%
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return root
        visited = list()
        need_visit = [root, 'mark']
        res = list()
        
        while need_visit:
            node = need_visit.pop(0)
            if node == 'mark':
                res.append(visited[-1].val)
                if need_visit: node = need_visit.pop(0)
                else: break
                need_visit.append('mark')
            if node not in visited:
                visited.append(node)
                if node.left: 
                    need_visit.append(node.left)
                if node.right: 
                    need_visit.append(node.right)
        
        return res