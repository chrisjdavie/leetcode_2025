from collections import Counter
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for row in board:
            counts: Counter = Counter(row)
            for key, value in counts.items():
                if key != "." and value > 1:
                    return False

        for i in range(len(board)):
            counts: Counter = Counter(row[i] for row in board)
            for key, value in counts.items():
                if key != "." and value > 1:
                    return False

        for i_square in range(0,len(board),3):
            for j_square in range(0,len(board),3):
                counts: Counter = Counter(
                    board[i][j]
                    for i in range(i_square, i_square + 3)
                        for j in range(j_square, j_square + 3)
                )
                for key, value in counts.items():
                    if key != "." and value > 1:
                        return False

        return True
