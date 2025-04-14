from collections import Counter

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_count: Counter = Counter(nums)
        return nums_count.most_common(1)[0][0]
