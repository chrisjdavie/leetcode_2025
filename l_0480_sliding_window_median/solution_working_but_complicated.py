"""
this does work, and passes, but there's a cleaner way of reference
and size tracking
"""
from __future__ import annotations

from collections import deque, Counter
from heapq import heappush, heappop
from typing import List

class Slider:

    def __init__(self, window_size: int):
        self._smaller: list[int] = []
        self._size_smaller: int = 0
        self._larger: list[int] = []
        self._size_larger: int = 0

        self._to_remove_count: Counter = Counter()

        self._window_size: int = window_size
        self._nums_window: deque[int] = deque()

    def _prune(self):
        while self._smaller and self._to_remove_count[-self._smaller[0]] > 0:
            self._to_remove_count[-self._smaller[0]] -= 1
            heappop(self._smaller)
        while self._larger and self._to_remove_count[self._larger[0]] > 0:
            self._to_remove_count[self._larger[0]] -= 1
            heappop(self._larger)

    def _rebalance(self) -> None:
        if self._size_smaller > self._size_larger + 1:
            self._size_smaller -= 1
            heappush(self._larger, -heappop(self._smaller))
            self._size_larger += 1
        if self._size_larger > self._size_smaller:
            self._size_larger -= 1
            heappush(self._smaller, -heappop(self._larger))
            self._size_smaller += 1
        self._prune()

    def add(self, num: int) -> None:

        # always adding to the heap
        self._nums_window.append(num)
        if not self._smaller or num <= -self._smaller[0]:
            heappush(self._smaller, -num)
            self._size_smaller += 1
        else:
            heappush(self._larger, num)
            self._size_larger += 1
        self._prune()
        self._rebalance()

        # sometimes remove
        if len(self._nums_window) > self._window_size:
            to_remove: int = self._nums_window.popleft()
            if to_remove <= -self._smaller[0]:
                self._size_smaller -= 1
            else:
                self._size_larger -= 1
            self._to_remove_count[to_remove] += 1
            self._rebalance()

    def median(self) -> float:
        if self._size_smaller == self._size_larger:
            return float((-self._smaller[0] + self._larger[0])/2)
        return float(-self._smaller[0])


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

