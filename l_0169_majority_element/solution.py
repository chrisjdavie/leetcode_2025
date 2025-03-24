from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        cand: int = -10**9 - 1
        votes: int = 0

        for this_num in nums:
            if votes == 0:
                cand = this_num
            
            if this_num == cand:
                votes += 1
            else:
                votes -= 1

        return cand
