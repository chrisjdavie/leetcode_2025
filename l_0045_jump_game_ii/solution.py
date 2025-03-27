from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        jump_count: int = 0
        current_furthest: int = -1
        next_furthest: int = -1

        for dist, jump in enumerate(nums[:-1]):
            if dist + jump > next_furthest:
                next_furthest = dist + jump
            if dist >= current_furthest:
                jump_count += 1
                current_furthest = next_furthest

        return jump_count
    