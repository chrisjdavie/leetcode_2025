from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_max: int = -10**9 - 1
        dp: list[list[int | None]] = [[None for _ in nums] for _ in nums]

        # zeroth rank
        for i, n in enumerate(nums):
            dp[0][i] = n

        for j in range(1, len(nums)):
            for i in range(j, len(nums)):
                dp[j][i] = dp[j-1][i-1] + nums[i]

        return max(n for row in dp for n in row if n is not None)
