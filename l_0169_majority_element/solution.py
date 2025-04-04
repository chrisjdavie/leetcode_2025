"""
Moore's voting algorithm
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        latest: int = -10**9 - 1
        votes: int = -1

        for n in nums:
            if latest == n:
                votes += 1
            else:
                votes -= 1

            if votes < 1:
                latest = n
                votes = 1

        return latest
