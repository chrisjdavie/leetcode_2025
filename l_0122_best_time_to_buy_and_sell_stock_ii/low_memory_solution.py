from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cuml_profit: int = 0

        for i in range(len(prices) - 1):
            if (delta := prices[i+1] - prices[i]) > 0:
                cuml_profit += delta

        return cuml_profit
