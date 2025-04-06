from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums_tmp = nums.copy()

        for i, this_num in enumerate(nums_tmp):
            i_rot = (i + k)%len(nums)
            nums[i_rot] = this_num
