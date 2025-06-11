from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        max_sub: int = -10**9 - 1
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                max_sub = max((max_sub, sum(nums[i:j])))

        return max_sub
