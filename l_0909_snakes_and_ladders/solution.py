from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        # flatten
        linear_board: list[int] = []

        reverse_toggle: bool = False

        for row in board[::-1]:
            linear_board.extend(row) if not reverse_toggle else linear_board.extend(row[::-1])
            reverse_toggle: bool = not reverse_toggle

        # zero index
        linear_board = [l-1 if l != -1 else l for l in linear_board]

        # bfs as only interested in the minimum number of moves it takes to
        # reach a given square

        # position, moves
        queue: deque[int,int] = deque([(0, 0)])

        # only have to visit each square once, as the first time will be the
        # fewest number of moves to get there (bfs)
        visited = {0,}

        while queue:

            position, moves = queue.popleft()
            
            furthest_ordinary: int = 0
            for step in range(1 + position, 7 + position):
                if step in visited:
                    continue
                visited.add(step)

                dest: int = linear_board[step]

                if step == len(linear_board) - 1 or dest == len(linear_board) - 1:
                    return moves + 1
                if dest == -1:
                    furthest_ordinary = step
                else:
                    queue.append((dest, moves + 1))

            if furthest_ordinary:
                queue.append((furthest_ordinary, moves + 1))

        return -1
