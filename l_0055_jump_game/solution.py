"""
Optimized based on others solutions in the forums, faster - doesn't use
max, slightly fewer operations probably

I'd say mine is clearer
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        max_dist: int = 0

        for dist in nums:
            if max_dist < 0:
                return False
            if dist > max_dist:
                max_dist = dist
            max_dist -= 1

        return True
