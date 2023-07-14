from typing import List

class Solution:
    """
        Top Interview 150 (BinaryTree BFS/ Medium)
        79. Word Search
        link : https://leetcode.com/problems/word-search/
        Date : July 14, 2023
        
        Runtime : 5945 ms, faster than 77.75%
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(start, row, col):
            if start == len(word):
                return True

            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != word[start]:
                return False

            board[row][col] = "#"
            start += 1
            found = (backtrack(start, row, col+1) or 
                    backtrack(start, row, col-1) or
                    backtrack(start, row+1, col) or
                    backtrack(start, row-1, col))
            board[row][col] = word[start-1]
            return found

        for row in range(m):
            for col in range(n):
                if word[0] == board[row][col]:
                    if backtrack(0, row, col): return True
                    
        return False