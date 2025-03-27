"""
Optimisation attempt - the slice operation duplicates array, uses 
a lot of memory. This uses less. But it's slower than slicing,
which wasn't expected

(according to leetcode statistics)

looking at the fastest code, it 
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cuml_profit: int = 0

        for i in range(len(prices) - 1):
            if (delta := prices[i+1] - prices[i]) > 0:
                cuml_profit += delta

        return cuml_profit
