"""
Should be NlogN time (all operations)
"""
from statistics import median

class MedianFinder:

    def __init__(self):
        self._numbers: list[int] = []

    def addNum(self, num: int) -> None:
        self._numbers.append(num)

    def findMedian(self) -> float:
        return median(self._numbers)
