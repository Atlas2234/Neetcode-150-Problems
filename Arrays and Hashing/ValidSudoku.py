"""
Time complexity is O(n^2).
Space complexity is O(n) due to the additional data structures used to track seen numbers in rows, columns, and squares.

"""

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Use defaultdict to automatically handle missing keys
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        # Iterate through each cell in the 9x9 board
        for r in range(9):
            for c in range(9):
                # Skip empty cells
                if board[r][c] == ".":
                    continue
                # Check for duplicates in the current row, column, and 3x3 square
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    # Calculate square index using integer division
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    # If a duplicate is found, return False
                    return False
                
                # Add the number to the respective row, column, and square sets
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True