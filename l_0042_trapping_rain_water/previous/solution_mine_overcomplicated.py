"""

"""
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        incline: bool = True

        maxima_height: List[tuple[int, int]] = []
        # find heights of maxima
        for i, (h, h_p_1) in enumerate(zip(height[:-1], height[1:])):
            if h < h_p_1:
                incline = True
            if h > h_p_1:
                if incline:
                    maxima_height.append((i, h))
                incline = False
        else:
            if incline:
                maxima_height.append((i+1, h_p_1))

        decline: True

        maxima_height_red: List[tuple[int, int]] = [maxima_height[0]]

        i_lhs: int = 0
        i_rhs_cand: int = i_lhs + 1

        while i_rhs_cand < len(maxima_height):
            for i_rhs in range(i_lhs + 1, len(maxima_height)):
                if maxima_height[i_rhs][1] >= maxima_height_red[-1][1]:
                    maxima_height_red.append(maxima_height[i_rhs])
                    i_lhs = i_rhs
                    i_rhs_cand = i_lhs + 1    
                    break
                if maxima_height[i_rhs][1] >= maxima_height[i_rhs_cand][1]:
                    i_rhs_cand = i_rhs
            else:
                maxima_height_red.append(maxima_height[i_rhs_cand])
                i_lhs = i_rhs_cand
                i_rhs_cand = i_lhs + 1

        total_water: int = 0

        for (i_max_0, height_0), (i_max_1, height_1) in zip(maxima_height_red[:-1], maxima_height_red[1:]):
            height_low: int = min((height_0, height_1))
            for h in height[i_max_0+1:i_max_1]:
                if h < height_low:
                    total_water += height_low - h

        return total_water
