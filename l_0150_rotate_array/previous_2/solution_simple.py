from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        for i, n in enumerate(nums.copy()):
            i_new: int = (i + k)%len(nums)
            nums[i_new] = n
