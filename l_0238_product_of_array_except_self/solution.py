"""
"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result: list[int] = [1]*len(nums)

        pref_prod: int = 1
        for i in range(len(nums)):
            result[i] = pref_prod
            pref_prod *= nums[i]
        
        suf_prod: int = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suf_prod
            suf_prod *= nums[i]

        return result
