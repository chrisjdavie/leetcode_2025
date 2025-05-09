from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        explored: List[List[bool]] = []

        for row in grid:
            explored.append([])
            for square in row:
                explored[-1].append(True if square == "0" else False)

        def fill_out(i, j):
            if i < 0 or i >= len(explored) or j < 0 or j >= len(explored[0]) or explored[i][j]:
                return

            explored[i][j] = True
            fill_out(i, j-1)
            fill_out(i, j+1)
            fill_out(i-1, j)
            fill_out(i+1, j)            

        islands: int = 0
        for i, row in enumerate(explored):
            for j, square in enumerate(row):
                if square is False:
                    fill_out(i, j)
                    islands += 1

        return islands
