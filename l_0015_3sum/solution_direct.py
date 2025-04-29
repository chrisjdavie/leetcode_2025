from itertools import combinations

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplet: set[tuple[int, int, int]] = set(
            tuple(sorted(comb))
            for comb in combinations(nums, 3)
                if sum(comb) == 0
        )

        return [list(comb) for comb in triplet]
