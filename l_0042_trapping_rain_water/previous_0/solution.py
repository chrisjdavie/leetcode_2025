"""
solution using a lot of Python
"""
from itertools import accumulate
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        left_highest: list[int] = accumulate(height, max)
        right_highest: list[int] = list(accumulate(height[::-1], max))[::-1]

        return sum(
            min((l_highest, r_highest)) - h
            for h, l_highest, r_highest 
                in zip(height, left_highest, right_highest)
        )
