"""
Simple solution
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
