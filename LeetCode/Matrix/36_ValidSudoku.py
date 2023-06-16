from typing import List
class Solution:
    """
        Top Interview 150 (Matrix/ Medium)
        36. Valid Sudoku
        link : https://leetcode.com/problems/valid-sudoku/
        Date : Jun 16, 2023
        
        Runtime : 121ms, faster than 36.18%
        used characteristics of set and list 
    """
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        numbers = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    numbers.append((i//3, j//3, board[i][j]))
                    numbers.append((-i, board[i][j]))
                    numbers.append((board[i][j],-j))

                #same logic
                # element = board[i][j]
                # if element != ".":
                #     numbers += [(i//3, j//3, element),(-i, element),(element,-j)]
        return len(numbers) == len(set(numbers))