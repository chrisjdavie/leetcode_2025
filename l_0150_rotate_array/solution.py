"""
using swaps and pivots
"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        for i in range(len(nums)//2):
            i_swp: int = len(nums) - 1 - i
            nums[i], nums[i_swp] = nums[i_swp], nums[i]
        
        for i in range(0, k//2):
            i_swp: int = k - 1 - i
            nums[i], nums[i_swp] = nums[i_swp], nums[i]

        for di in range((len(nums) - k)//2):
            i: int = k + di
            i_swp: int = len(nums) - 1 - di
            nums[i], nums[i_swp] = nums[i_swp], nums[i]
