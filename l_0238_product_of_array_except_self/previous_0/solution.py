"""
My solution worked first time, but this was in other people's submissions, and it's
a lot cleaner, and also shows a clearer mental model of the problem
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result: list[int] = [1]*len(nums)

        pref_product: int = 1
        for i in range(len(nums)):
            result[i] *= pref_product
            pref_product *= nums[i]

        suf_product: int = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suf_product
            suf_product *= nums[i]

        return result

