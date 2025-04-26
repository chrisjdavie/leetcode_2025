"""
using swaps and pivots
"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k_piv: int = k%len(nums)

        for i in range(len(nums)//2):
            nums[i], nums[-i-1] = nums[-i-1], nums[i]

        for i in range(k_piv//2):
            nums[i], nums[k_piv-i-1] = nums[k_piv-i-1], nums[i]

        for i in range((len(nums) - k_piv)//2):
            nums[k_piv+i], nums[-i-1] = nums[-i-1], nums[k_piv+i]
