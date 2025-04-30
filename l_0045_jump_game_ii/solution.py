from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:

        prev_max_dist: int = 0
        next_max_dist: int = 0
        jump_counter: int = 0

        for i, n in enumerate(nums[:-1]):
            next_max_dist = max((next_max_dist, n + i))
            if i == prev_max_dist:
                jump_counter += 1
                prev_max_dist = next_max_dist
    
        return jump_counter
