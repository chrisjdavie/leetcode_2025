from collections import defaultdict

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        nums_count: dict[int, int] = defaultdict(int)

        for n in nums:
            nums_count[n] += 1
            if nums_count[n] >= (len(nums) + 1)//2:
                break

        return n
