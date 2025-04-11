"""
Super simple solution, but very slow
"""
from itertools import combinations

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        unique_combs = set()
        for comb in combinations(sorted(nums), 3):
            if sum(comb) == 0:
                unique_combs.add(comb)

        return [list(comb) for comb in unique_combs]
