from collections import deque

from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        # linearise board
        linear_board: List[int] = []
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
            
            furthest_ordinary: int = 0
            for step in range(pos+1, pos+7):
                if step in visited:
                    continue
                visited.add(step)

                dest: int = linear_board[step]
                if dest == len(linear_board) - 1 or step == len(linear_board) - 1:
                    return moves + 1
                if dest == -1:
                    furthest_ordinary = step
                else:
                    queue.append((moves+1, dest))
            if furthest_ordinary:
                queue.append((moves+1, furthest_ordinary))

        return -1
