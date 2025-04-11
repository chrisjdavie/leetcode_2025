from collections import Counter
from itertools import product

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_count: Counter[int, int] = Counter(nums)
        nums_positive: set[int] = {n for n in nums if n > 0}
        nums_negative: set[int] = {n for n in nums if n < 0}

        result: set[tuple[int, int, int]] = set()
        if nums_count[0] >= 3:
            result.add((0,0,0))

        for n_neg, n_pos in product(nums_negative, nums_positive):
            if (opp := -(n_neg + n_pos)) in nums_count:
                if opp == n_pos or opp == n_neg:
                    if nums_count[opp] < 2:
                        continue
                result.add(tuple(sorted((n_neg, opp, n_pos))))

        return [list(r) for r in result]
