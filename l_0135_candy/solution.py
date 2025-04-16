"""
Optimised version of the previous
"""
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # length 1
        if len(ratings) == 1:
            return 1

        results: list[int] = [1]*len(ratings)

        prev_candy: int = 1
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                prev_candy += 1
                results[i] = prev_candy
            else:
                prev_candy = 1

        prev_candy: int = 1
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i+1] < ratings[i]:
                prev_candy += 1
                if prev_candy > results[i]:
                    results[i] = prev_candy
            else:
                prev_candy = 1

        return sum(results)
