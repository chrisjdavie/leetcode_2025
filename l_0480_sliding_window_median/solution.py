"""
Inspired by someone else's answer from leetcode, incorporated into
the interview form

This, I think, reflects the best one, it incoorporates two bits of knowledge.
The first is that, each removing and adding to the list can only move the
median one position (independently), and so you can lazy-delete.

The other (that comes from the above) is that, once you have the window full,
if you add and remove from different sides, you need to shift the numbers in
stack to retain the balance between the cleaned heaps
"""
from collections import deque
from heapq import heappush, heappop

from typing import List


class SlidingWindow:

    def __init__(self, window_size: int):
        self._window_size: int = window_size
        self._count: int = 0

        self._numbers: deque[tuple[int,int]] = deque()

        self._smaller: list[int] = []
        self._larger: list[int] = []

    def add(self, num):
        if self._window_size == 1:
            self._smaller = [(-num, -1)]
            return

        # building up the first n numbers
        if len(self._numbers) < self._window_size:
            self._numbers.append(num)
            heappush(self._smaller, (-num, self._count))
            self._count += 1

            # set up the stacks once
            if self._count == self._window_size:
                while len(self._smaller) > len(self._larger) + 1:
                    num_mv, idx = heappop(self._smaller)
                    heappush(self._larger, (-num_mv, idx))            
        else:
            # add new number, while retaining heap balance
            self._numbers.append(num)
            num_remove: int = self._numbers.popleft()
            if num <= -self._smaller[0][0]:
                heappush(self._smaller, (-num, self._count))
                if num_remove >= self._larger[0][0]:
                    num_mv, idx = heappop(self._smaller)
                    heappush(self._larger, (-num_mv, idx))
            else:
                heappush(self._larger, (num, self._count))
                if num_remove <= -self._smaller[0][0]:
                    num_mv, idx = heappop(self._larger)
                    heappush(self._smaller, (-num_mv, idx))
            self._count += 1

            # lazy delete old numbers
            while self._smaller[0][1] < self._count - self._window_size:
                heappop(self._smaller)
            while self._larger[0][1] < self._count - self._window_size:
                heappop(self._larger)

    def median(self):
        if self._window_size % 2:
            return float(-self._smaller[0][0])
        return float((-self._smaller[0][0] + self._larger[0][0])/2)

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        
        sw: SlidingWindow = SlidingWindow(k)

        for n in nums[:k-1]:
            sw.add(n)
        
        results: list[int] = []
        for n in nums[k-1:]:
            sw.add(n)
            results.append(sw.median())

        return results
