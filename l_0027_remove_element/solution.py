from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        count: int = 0

        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
            else:
                i_rep = i - count
                nums[i_rep] = nums[i]

        return len(nums) - count
