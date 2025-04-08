"""
"""
from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count: Counter = Counter(nums)
        for n, count in nums_count.items():
            if count > len(nums)//2:
                break
        return n
