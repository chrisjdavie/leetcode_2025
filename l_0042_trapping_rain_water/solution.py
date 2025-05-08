from itertools import accumulate
from typing import List, Iterator

class Solution:
    def trap(self, height: List[int]) -> int:

        max_height_left: Iterator[int] = accumulate(height, max)
        max_height_right: list[int] = list(accumulate(height[::-1], max))
        max_height_right.reverse()

        return sum(
            min((mhl, mhr)) - h for h, mhl, mhr in zip(height, max_height_left, max_height_right)
        )
