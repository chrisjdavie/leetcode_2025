"""
This isn't working, I'm going to revisit the median tomorrow from a
different direction
"""
from collections import deque
from heapq import heappush, heappop
from typing import List

class Slider:

    def __init__(self, window_size: int):
        self._smaller: list[tuple[int,int]] = []
        self._larger: list[tuple[int,int]] = []

        self._count: int = 0
        self._window_size: int = window_size
        self._nums_window: deque[int] = deque()

    def _prune(self):
        while self._smaller and self._smaller[0][1] < self._count - self._window_size:
            heappop(self._smaller)
        while self._larger and self._larger[0][1] < self._count - self._window_size:
            heappop(self._larger)

    def add(self, num: int) -> None:

        # sometimes remove
        to_remove: int | None = None
        if len(self._nums_window) > self._window_size:
            to_remove = self._nums_window.popleft()

        # always adding to the heap
        self._nums_window.append(num)
        if not self._smaller or num <= -self._smaller[0][0]:
            heappush(self._smaller, (-num, self._count))
        else:
            heappush(self._larger, (num, self._count))

        self._count += 1

    def median(self) -> float:
        if not self._window_size % 2:
            return float((-self._smaller[0][0] + self._larger[0][0])/2)
        return float(-self._smaller[0][0])


class Solution:

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        slider = Slider(k)
        for n in nums[:k-1]:
            slider.add(n)

        results: list[float] = []
        for n in nums[k-1:]:
            slider.add(n)
            results.append(slider.median())

        return results
