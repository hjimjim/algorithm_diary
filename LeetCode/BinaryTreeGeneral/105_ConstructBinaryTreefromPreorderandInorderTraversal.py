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
        105. Construct Binary Tree from Preorder and Inorder Traversal
        link : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
        Date : July 7, 2023
        
        Runtime : 219 ms, faster than 22.18%
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        length = len(preorder)
        current_root = preorder[0]
        if length == 1: return TreeNode(inorder[0], None, None)
        croot_index = inorder.index(current_root)

        if croot_index == 0:
            # no left yes right
            right_node = self.buildTree(preorder[croot_index + 1:], inorder[croot_index + 1:])
            return TreeNode(current_root, None, right_node)
        elif croot_index+1 == length:
            # no right
            left_node = self.buildTree(preorder[1:croot_index+1], inorder[:croot_index])
            return TreeNode(current_root, left_node, None)
        elif croot_index + 1 < length:
            # left and right
            right_node = self.buildTree(preorder[croot_index + 1:], inorder[croot_index + 1:])
            left_node = self.buildTree(preorder[1:croot_index+1], inorder[:croot_index])
            return TreeNode(current_root, left_node, right_node)