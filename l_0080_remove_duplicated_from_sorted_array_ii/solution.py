from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        current_num: int = -10**4 - 1
        count: int = -1
        i_insert: int = 0

        for n in nums:
            if n != current_num:
                current_num = n
                count = 0
            if count < 2:
                nums[i_insert] = n
                i_insert += 1
            count += 1

        return i_insert
