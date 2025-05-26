from collections import deque

from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        # linearise board
        linear_board: list[int] = []
        reverse_toggle: bool = False

        for row in board[::-1]:
            linear_board.extend(row) if not reverse_toggle else linear_board.extend(row[::-1])
            reverse_toggle = not reverse_toggle

        # zero index
        linear_board = [l-1 if l != -1 else l for l in linear_board]

        queue: deque[tuple[int,int]] = deque([(0, 0)])
        visited: set[int] = {0,}

        while queue:
            moves, pos = queue.popleft()

            furthest_ordinary: int | None = None
            for step in range(pos+1, pos+7):
                if step in visited:
                    continue
                visited.add(step)
                if step == len(linear_board) - 1 or linear_board[step] == len(linear_board) - 1:
                    return moves + 1
                if linear_board[step] == -1:
                    furthest_ordinary = step
                else:
                    queue.append((moves+1, linear_board[step]))
            if furthest_ordinary is not None:
                queue.append((moves+1, furthest_ordinary))

        return -1
