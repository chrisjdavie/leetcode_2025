from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges: list[str] = []

        n_start: int = nums[0]
        n_end: int = nums[0]

        for n in nums[1:] + [1002]:
            if n != n_end + 1:
                if n_start == n_end:
                    ranges.append(str(n_start))
                else:
                    ranges.append(str(n_start) + "->" + str(n_end))
                n_start = n
            n_end = n

        return ranges
