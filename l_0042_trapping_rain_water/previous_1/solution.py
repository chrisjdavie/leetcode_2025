from itertools import accumulate
from typing import List, Iterator

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        left_max_height: Iterator[int] = accumulate(height, max)
        right_max_height: List[int] = list(accumulate(height[::-1], max))[::-1]

        return sum(
            min((l_m_h, r_m_h)) - h
            for h, l_m_h, r_m_h in zip(height, left_max_height, right_max_height)
        )
