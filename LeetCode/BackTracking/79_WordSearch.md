## Understand problems better by thinking about complex cases.
- can not visit the same cell that is already visited
- can only visit cells horizontally or vertically neighboring
 
## Write the solution in human language 
1. loop word and find the current letter in the board
2. if the current letter is found from neighbors
    2.1. find letter from neighbors
        if current letter == board[current_y, current_x+1]
        or board[current_y+1, current_x]
3. move to cell found
      
## Make draft code
```
def backTrack():
    loop word and get current_letter
        if current_letter == board[current_y, current_x+1]:
            delete number from next cell
            backTrack
        if current_letter == board[current_y+1, current_x]
            delete number from next cell
            backTrack
```
## Write code
the code below has duplicate code and is not efficient
time out example :
- board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
- word = "aaaaaaaaaaaaa"

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backTrack(start, row, col, new_board):
            if start == len(word):
                return True

            if row < 0 or row >= m or col < 0 or col >= n:
                return False

            for current_letter in word[start:]:
                if col < n - 1 and current_letter == new_board[row][col+1]:
                    #right
                    new_board[row][col+1] = "None" 
                    if backTrack(start+1, row, col+1, new_board): return True
                    new_board[row][col+1] = current_letter
                if col > 0 and current_letter == new_board[row][col-1]:
                    #left
                    new_board[row][col-1] = "None" 
                    if backTrack(start+1, row, col-1, new_board): return True
                    new_board[row][col-1] = current_letter
                if row < m - 1 and current_letter == new_board[row+1][col]:
                    #down
                    new_board[row+1][col] = "None" 
                    if backTrack(start+1, row+1, col, new_board): return True
                    new_board[row+1][col] = current_letter
                if row > 0 and current_letter == new_board[row-1][col]:
                    #up
                    new_board[row-1][col] = "None" 
                    if backTrack(start+1, row-1, col, new_board): return True
                    new_board[row-1][col] = current_letter
            return False
        for row in range(m):
            for col in range(n):
                if word[0] == board[row][col]:
                    board[row][col] = "None"
                    if backTrack(1, row, col ,board): return True
                    board[row][col] = word[0]
                    
        return False
```

## Look for improvements

``` python
class Solution:
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
```
