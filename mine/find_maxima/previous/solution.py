from typing import List

def find_maxima(height: List[int]) -> int:
    incline: bool = True

    maximas: list[int] = []

    for i, (h, h_p_1) in enumerate(zip(height[:-1], height[1:])):
        if h < h_p_1:
            incline = True
        if h > h_p_1 and incline:
            maximas.append(i)
            incline = False

    return maximas
