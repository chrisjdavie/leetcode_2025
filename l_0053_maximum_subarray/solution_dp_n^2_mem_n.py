from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curr_max: int = -10**9 - 1
        dp: list[list[int | None]] = [[None for _ in nums] for _ in range(2)]
        toggle: bool = True

        # zeroth rank
        for i, n in enumerate(nums):
            dp[0][i] = n
            if dp[0][i] > curr_max:
                curr_max = dp[0][i]

        for j in range(1, len(nums)):
            j_curr: int = 0
            j_prev: int = 1
            if toggle:
                j_curr: int = 1
                j_prev: int = 0
            for i in range(j, len(nums)):
                dp[j_curr][i] = dp[j_prev][i-1] + nums[i]
                if dp[j_curr][i] > curr_max:
                    curr_max = dp[j_curr][i]
            toggle = not toggle

        return curr_max
