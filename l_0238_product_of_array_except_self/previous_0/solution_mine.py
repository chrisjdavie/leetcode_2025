from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output: list[int] = [1]*len(nums)
        
        prev_prod: int = 1
        for i_rev in range(len(nums) - 1, 0, -1):
            i_in_rev: int = i_rev - 1
            prev_prod = nums[i_rev]*prev_prod
            output[i_in_rev] = prev_prod

        prev_prod: int = 1
        for i_for in range(len(nums) - 1):
            i_in_for: int = i_for + 1
            prev_prod = nums[i_for]*prev_prod
            output[i_in_for] = output[i_in_for]*prev_prod

        return output
