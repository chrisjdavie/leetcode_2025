from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        for i, cit in enumerate(citations):
            if i >= cit:
                return i
        return len(citations)
    