from itertools import combinations

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result: set[tuple] = set()

        for comb in combinations(nums, 3):
            if sum(comb) == 0:
                result.add(tuple(sorted(comb)))

        return [list(comb) for comb in result]
