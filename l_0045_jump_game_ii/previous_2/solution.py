from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        jumps: int = 0
        current_furthest: int = 0
        next_furthest: int = 0

        for i, dist in enumerate(nums[:-1]):
            if i + dist > next_furthest:
                next_furthest = i + dist
            if i == current_furthest:
                jumps += 1
                current_furthest = next_furthest

        return jumps
