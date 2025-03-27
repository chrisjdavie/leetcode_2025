"""
Optimisation attempt - the slice operation duplicates array, uses 
a lot of memory. This uses less.

So this is faster than using the walrus, I guess maybe writing
to a variable each loop is expensive compared to this? But it's
all O(N), and leetcode says this is higher memory useage, so it'd
be interesting to see what the test cases are.

I'm happy I can recreate behaviours, so onto the next
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cuml_profit: int = 0

        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                cuml_profit += prices[i+1] - prices[i]

        return cuml_profit
