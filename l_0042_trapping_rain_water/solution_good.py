from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0

        left_highest: list[int] = []
        current_highest: int = 0

        for h in height:
            if h > current_highest:
                current_highest = h
            left_highest.append(current_highest)
        
        right_highest: list[int] = []
        current_highest: int = 0
        for h in height[::-1]:
            if h > current_highest:
                current_highest = h
            right_highest.append(current_highest)
        right_highest.reverse()

        total_water: int = 0
        for h, l_highest, r_highest in zip(height, left_highest, right_highest):
            total_water += min((l_highest, r_highest)) - h

        return total_water
