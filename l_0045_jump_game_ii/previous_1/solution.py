from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        current_furthest: int = 0
        next_furthest: int = 0
        min_jumps: int = 0

        for i, n in enumerate(nums[:-1]):
            if i + n > next_furthest:
                next_furthest = i + n
            if i == current_furthest:
                current_furthest = next_furthest
                min_jumps += 1

        return min_jumps
