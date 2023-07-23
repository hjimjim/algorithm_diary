class Solution:
    """
        Top Interview 150 (Array/ Medium)
        11. Container With Most Water
        link : https://leetcode.com/problems/container-with-most-water/
        Date : July 23, 2023
        
        Runtime : 656ms, faster than 92.82%
    """
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) -1
        maxHeight = 0
        while left < right: 
            if height[left] < height[right]:
                tempHeight = height[left] * (right - left)
                left += 1
            else:
                tempHeight = height[right] * (right - left)
                right -= 1

            if maxHeight < tempHeight:
                maxHeight = tempHeight
        
        return maxHeight
                