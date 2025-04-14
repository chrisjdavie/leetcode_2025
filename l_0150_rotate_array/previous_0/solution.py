"""
Solution from the forums - in place, so O(1) ish memory, but 
"""
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)

        # reverse first half
        swaps: list[tuple[int]] = [
            (0, len(nums) - k - 1),
            (len(nums) - k, len(nums) - 1),
            (0, len(nums) - 1)
        ]

        for i_start, i_end in swaps:
            for di in range(0, (i_end + 1 - i_start)//2):
                nums[i_start + di], nums[i_end - di] = nums[i_end - di], nums[i_start + di]
