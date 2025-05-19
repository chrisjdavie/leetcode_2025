"""
Should be NlogN time (all operations)
"""
from heapq import heappop, heappush

class MedianFinder:

    def __init__(self):
        self._smaller: list[int] = []
        self._larger: list[int] = []

    def addNum(self, num: int) -> None:
        if not self._smaller or num <= -self._smaller[0]:
            heappush(self._smaller, -num)
            if len(self._smaller) > len(self._larger) + 1:
                heappush(self._larger, -heappop(self._smaller))
        else:
            heappush(self._larger, num)
            if len(self._larger) > len(self._smaller):
                heappush(self._smaller, -heappop(self._larger))

    def findMedian(self) -> float:
        if len(self._smaller) == len(self._larger):
            return float((-self._smaller[0] + self._larger[0])/2)
        return float(-self._smaller[0])
