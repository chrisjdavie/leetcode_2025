from collections import Counter
from itertools import product

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums_count: Counter = Counter(nums)

        nums_neg: set[int] = set(n for n in nums if n < 0)
        nums_pos: set[int] = set(n for n in nums if n > 0)

        uniq_triplets: set[tuple[int, int, int]] = set()

        if nums_count[0] >= 3:
            uniq_triplets.add((0,0,0))

        for n_neg, n_pos in product(nums_neg, nums_pos):
            if (opp := -(n_neg + n_pos)) in nums_count:
                if (opp == n_neg or opp == n_pos) and nums_count[opp] < 2:
                    continue
                uniq_triplets.add(tuple(sorted([n_neg, opp, n_pos])))
        
        return [list(trip) for trip in uniq_triplets]
