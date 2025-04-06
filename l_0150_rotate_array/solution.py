"""
Using swaps and a pivot
"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        for i_lhs in range(len(nums)//2):
            i_rhs: int = len(nums) - i_lhs - 1
            nums[i_lhs], nums[i_rhs] = nums[i_rhs], nums[i_lhs]

        for i_lhs in range(k//2):
            i_rhs: int = k - i_lhs - 1
            nums[i_lhs], nums[i_rhs] = nums[i_rhs], nums[i_lhs]

        for di in range((len(nums) - k)//2):
            i_lhs: int = k + di
            i_rhs: int = len(nums) - di - 1
            nums[i_lhs], nums[i_rhs] = nums[i_rhs], nums[i_lhs]
