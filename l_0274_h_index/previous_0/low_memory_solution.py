"""
This is in-place, using sorts, not creating new data structures

It is O(1) additional memory and O(NlogN) time due to sorting
"""
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        for i, cit in enumerate(citations):
            if i >= cit:
                return i
        return len(citations)
