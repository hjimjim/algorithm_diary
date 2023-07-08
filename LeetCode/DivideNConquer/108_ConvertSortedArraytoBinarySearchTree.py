from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """
        Top Interview 150 (BinarySearchTree/ Easy)
        108. Convert Sorted Array to Binary Search Tree
        link : https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
        Date : July 8, 2023
        
        Runtime : 77 ms, faster than 49.21%
    """
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 1:
            return TreeNode(nums[0], None, None)
        if len(nums) == 2:
            return TreeNode(nums[1], TreeNode(nums[0], None, None), None)

        index = len(nums)//2
        return TreeNode(nums[index], self.sortedArrayToBST(nums[:index]), self.sortedArrayToBST(nums[index+1:]))