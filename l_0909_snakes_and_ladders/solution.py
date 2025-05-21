from typing import List

def pos_to_coords(pos: int, width: int) -> tuple[int, int]:
    row: int = width - 1 - (pos - 1) // width
    col: int = (pos - 1) % width
    if ((pos - 1) // width) % 2:
        col = width - col - 1
    return row, col


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        return -2
