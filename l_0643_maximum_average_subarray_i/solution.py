from typing import List, Iterator


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        nums_add: Iterator[int] = iter(nums)
        nums_remove: Iterator[int] = iter(nums)

        running_total: int = 0

        for _ in range(k):
            running_total += next(nums_add)

        maximum_total: int = running_total

        for n_add, n_remove in zip(nums_add, nums_remove):
            running_total = running_total + n_add - n_remove
            if running_total > maximum_total:
                maximum_total = running_total

        return maximum_total / k
