from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n: int = len(citations)

        cit_count: list[int] = [0 for _ in range(n + 1)]

        for cit in citations:
            if cit > n:
                cit_count[n] += 1
            else:
                cit_count[cit] += 1

        print(cit_count)

        running_total: int = 0

        for cand_h_index in range(n, -1, -1):
            running_total += cit_count[cand_h_index]
            if running_total >= cand_h_index:
                break
        
        return cand_h_index
    