from collections import deque
from itertools import zip_longest
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        # linearise
        linear_board: List[int] = []

        for row_odd, row_even in zip_longest(board[::-2], board[-2::-2], fillvalue=[]):
            for square in row_odd:
                if square != -1:
                    linear_board.append(square - 1)
                else:
                    linear_board.append(square)
            for square in row_even[::-1]:
                if square != -1:
                    linear_board.append(square - 1)
                else:
                    linear_board.append(square)

        LARGE_TURNS: int = len(board)**2 + 1 # bigger than max possible turns
        turns_min: int = LARGE_TURNS

        visited: set[int] = set()
        # dfs
        def _dfs(pos: int, turns: int) -> None:
            nonlocal turns_min
            # no point in exploring if a better answer is found
            if turns >= turns_min:
                return
            # already visited, will not reduce the number of turns
            if pos in visited:
                return
            visited.add(pos) # do not pop, as we are exploring furthest first

            # if you land on the final square, you don't take another turn
            if pos == len(linear_board) - 1:
                # finished exploration of this node
                turns_min = min((turns_min, turns))
                visited.remove(pos)                
                return

            final_minus_1_step: int | None = None
            for step in range(1, 7):
                if step + pos == len(linear_board) - 1:
                    turns_min = min((turns_min, turns + 1))
                    visited.remove(pos)
                    return
                if linear_board[step + pos] != -1:
                    _dfs(linear_board[step + pos], turns + 1)
                else:
                    final_minus_1_step = step

            if final_minus_1_step:
                _dfs(pos + final_minus_1_step, turns + 1)

            # finished exploration of this node
            visited.remove(pos)
            return 

        _dfs(0,0)
        if turns_min >= LARGE_TURNS:
            return -1
        return turns_min
