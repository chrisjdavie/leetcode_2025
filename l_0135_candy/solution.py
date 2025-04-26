"""
"""
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:

        prev_rating: int = -1
        candy: int = 0

        left_candy: list[int] = []
        for rat in ratings:
            if rat > prev_rating:
                candy += 1
            else:
                candy = 1
            left_candy.append(candy)
            prev_rating = rat

        prev_rating: int = -1
        candy: int = 0

        right_candy: list[int] = []
        for rat in ratings[::-1]:
            if rat > prev_rating:
                candy += 1
            else:
                candy = 1
            right_candy.append(candy)
            prev_rating = rat
        right_candy.reverse()

        return sum(max((l_c, r_c)) for l_c, r_c in zip(left_candy, right_candy))
