"""
Optimized based on others solutions in the forums, faster - doesn't use
max, slightly fewer operations probably

I'd say mine is clearer
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        ind_furthest: int = 0

        for i, n in enumerate(nums[:-1]):
            if i + n > ind_furthest:
                ind_furthest = i + n
            if ind_furthest <= i:
                return False

        return True
