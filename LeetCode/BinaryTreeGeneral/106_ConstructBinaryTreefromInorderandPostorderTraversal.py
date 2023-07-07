from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Top Interview 150 (BinaryTree/ Easy)
        106. Construct Binary Tree from Inorder and Postorder Traversal
        link : https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
        Date : July 7, 2023
        
        Runtime : 253 ms, faster than 11.75%
    """
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        length = len(postorder)
        current_root = postorder[-1]
        if length == 1: return TreeNode(current_root, None, None)
        croot_index = inorder.index(current_root)

        if croot_index == 0:
            # no left yes right
            right_node = self.buildTree(inorder[croot_index + 1:], postorder[croot_index:-1])
            return TreeNode(current_root, None, right_node)
        elif croot_index+1 == length:
            # no right
            left_node = self.buildTree(inorder[:croot_index], postorder[:croot_index])
            return TreeNode(current_root, left_node, None)
        elif croot_index + 1 < length:
            # left and right
            right_node = self.buildTree(inorder[croot_index + 1:], postorder[croot_index:-1])
            left_node = self.buildTree(inorder[:croot_index], postorder[:croot_index])
            return TreeNode(current_root, left_node, right_node)
        
