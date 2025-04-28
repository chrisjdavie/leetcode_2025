"""
"""
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)

        for h, cit in enumerate(citations):
            if h + 1 > cit:
                h_index: int = h
                break
        else:
            h_index: int = len(citations)

        return h_index
