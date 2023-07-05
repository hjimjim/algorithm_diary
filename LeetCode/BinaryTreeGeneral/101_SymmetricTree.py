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
        101. Symmetric Tree
        link : https://leetcode.com/problems/symmetric-tree/
        Date : July 5, 2023
        
        Runtime : 40 ms, faster than 95.81%
    """

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(left, right):
            if not left and not right: return True
            if not left or not right: return False
            return left.val == right.val and check(left.right,right.left) and check(left.left, right.right)        

        return check(root, root)
    
    # def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    #     if not root: return root
    #     if not root.left and not root.right: return root
    #     else:
    #         root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    #         return root
    
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q: return True
    #     if not p or not q: return False
    #     return p.val == q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)
    
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     if not root: 
    #         return True
    #     if not root.left and not root.right:
    #         return True
    #     else:
    #         return self.isSameTree(root.left, self.invertTree(root.right))
        
        