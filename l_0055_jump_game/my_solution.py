from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_dist: int = 0

        for i, dist in enumerate(nums):
            if max_dist < i:
                return False

            max_dist = max((max_dist, i + dist))

        return True
