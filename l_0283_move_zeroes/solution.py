from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i_insert: int = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            nums[i_insert] = nums[i]
            i_insert += 1

        for i in range(i_insert, len(nums)):
            nums[i] = 0
