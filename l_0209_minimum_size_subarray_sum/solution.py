from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i_lhs: int = 0
        i_rhs: int = 0
        total_window: int = 0

        min_length: int = len(nums) + 1

        while True:
            if total_window >= target:
                total_window -= nums[i_lhs]
                i_lhs += 1
            else:
                if i_rhs == len(nums):
                    break
                total_window += nums[i_rhs]
                i_rhs += 1
            if total_window >= target:
                min_length = min((min_length, i_rhs - i_lhs))

        if min_length > len(nums):
            return 0
        return min_length
