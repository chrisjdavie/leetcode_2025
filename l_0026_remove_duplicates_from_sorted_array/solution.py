from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count: int = 0
        prev_num: int = -101

        for this_num in nums:
            if this_num != prev_num:
                nums[count] = this_num
                prev_num = this_num
                count += 1

        return count
    