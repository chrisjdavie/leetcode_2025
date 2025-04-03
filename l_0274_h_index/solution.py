"""
This uses a hashmap to be O(N) time, guess O(N) memory as well?
"""
from collections import Counter
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations_count: Counter = Counter(citations)

        running_total: int = 0

        num_citations: int = 0
        for num_citations in range(max(citations_count.keys()), -1, -1):
            running_total += citations_count[num_citations]
            if running_total >= num_citations:
                break

        return num_citations
