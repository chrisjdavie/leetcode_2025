from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        citations.sort(reverse=True)
        for cand_h_index, cit in enumerate(citations):
            if cand_h_index >= cit:
                break
        else:
            cand_h_index += 1

        return cand_h_index
