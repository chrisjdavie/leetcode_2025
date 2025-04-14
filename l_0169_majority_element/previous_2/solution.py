"""
Moore's voting algorithm
"""
from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        candidate: int = -10**9 - 1
        votes: int = 0

        for n in nums:
            if n == candidate:
                votes += 1
            else:
                votes -= 1
            
            if votes < 1:
                candidate = n
                votes = 1
        
        return candidate
