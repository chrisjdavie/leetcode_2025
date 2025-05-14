from collections import deque
from statistics import median
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if len(nums) < k:
            return []

        window: deque[int] = deque((n for n in nums[:k]))
        medians: List[float | int] = [median(window)]

        for n in nums[k:]:
            window.popleft()
            window.append(n)
            medians.append(median(window))

        return medians
