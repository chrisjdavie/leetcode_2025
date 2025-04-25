from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # length 1
        if len(ratings) == 1:
            return 1
        # length 2?

        l_to_r: list[int] = [1]*len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                l_to_r[i] = l_to_r[i-1] + 1

        r_to_l: list[int] = [1]*len(ratings)
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i+1] < ratings[i]:
                r_to_l[i] = r_to_l[i+1] + 1

        return sum([max((l, r)) for l, r in zip(l_to_r, r_to_l)])
