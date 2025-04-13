from itertools import combinations

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        neg_nums: list[int] = []
        neg_nums_set: set[int] = set()
        pos_nums: list[int] = []
        pos_nums_set: set[int] = set()

        zero_count: int = 0

        for n in sorted(nums):
            if n < 0:
                neg_nums.append(n)
                neg_nums_set.add(n)
            else:
                pos_nums.append(n)
                pos_nums_set.add(n)
            if n == 0:
                zero_count += 1

        unique_combs: set[tuple[int,int,int]] = set()
        if zero_count >= 3:
            unique_combs.add((0, 0, 0))

        for neg_comb in combinations(neg_nums, 2):
            if -sum(neg_comb) in pos_nums_set:
                unique_combs.add((neg_comb[0], neg_comb[1], -sum(neg_comb)))

        for pos_comb in combinations(pos_nums, 2):
            if -sum(pos_comb) in neg_nums_set:
                unique_combs.add((-sum(pos_comb), pos_comb[0], pos_comb[1]))

        return [list(comb) for comb in unique_combs]
