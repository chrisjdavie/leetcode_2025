"""
"""
from collections import Counter
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citation_count: Counter = Counter()

        for cit in citations:
            if cit >= len(citations):
                citation_count[len(citations)] += 1
            else:
                citation_count[cit] += 1

        running_total: int = 0
        for i in range(len(citations), -1, -1):
            running_total += citation_count[i]
            if running_total >= i:
                h_index: int = i
                break

        return h_index
