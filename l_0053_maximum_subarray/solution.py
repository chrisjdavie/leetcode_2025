"""
Taken from an example solution
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_max: int = -10**4 - 1
        sum_subarray: int = 0

        for n in nums:
            sum_subarray += n
            curr_max = max((curr_max, sum_subarray))

            if sum_subarray < 0:
                sum_subarray = 0

        return curr_max
