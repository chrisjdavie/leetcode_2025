from collections import Counter

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cand: int = nums[0]
        votes: int = 1

        for n in nums[1:]:
            if n == cand:
                votes += 1
            else:
                votes -= 1
                if votes == 0:
                    cand = n
                    votes = 1

        return cand
