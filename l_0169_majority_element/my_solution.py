"""
My first solution, nice and clear and uses inbuilts, not the first
"""

from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        counter = Counter(nums)
        return counter.most_common(1)[0][0]
