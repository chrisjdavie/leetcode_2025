from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        elements_count: int = 0
        value_count: int = 0
        prev_value: int = -10**4 - 1

        for i in range(len(nums)):
            this_value = nums[i]
            if this_value != prev_value:
                prev_value = this_value
                nums[elements_count] = prev_value
                elements_count += 1
                value_count = 0
            elif value_count < 1:
                nums[elements_count] = prev_value
                elements_count += 1
                value_count += 1

        return elements_count
