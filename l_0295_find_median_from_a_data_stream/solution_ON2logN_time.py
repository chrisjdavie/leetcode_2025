from statistics import median

class MedianFinder:

    def __init__(self):
        self._nums: list[int] = []

    def addNum(self, num: int) -> None:
        self._nums.append(num)

    def findMedian(self) -> float:
        return median(self._nums)
