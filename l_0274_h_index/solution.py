"""
O(N), but slow as Counters are slower than lists initialised to
zero in this case
"""
from collections import Counter
from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        binned_citations: Counter = Counter()

        for cit in citations:
            if cit >= len(citations):
                binned_citations[len(citations)] += 1
            else:
                binned_citations[cit] += 1

        running_total: int = 0

        for cand_h_index in range(len(citations), -1, -1):
            running_total += binned_citations[cand_h_index]
            if running_total >= cand_h_index:
                break

        return cand_h_index
