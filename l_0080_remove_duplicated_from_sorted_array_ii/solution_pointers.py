from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i_insert: int = 0

        for n in nums:
            if i_insert <= 1 or n != nums[i_insert - 2]:
                nums[i_insert] = n
                i_insert += 1

        return i_insert
