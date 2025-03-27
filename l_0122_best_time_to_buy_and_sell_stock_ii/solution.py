from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cuml_profit: int = 0

        for price_0, price_1 in zip(prices[:-1], prices[1:]):
            if (delta := price_1 - price_0) > 0:
                cuml_profit += delta

        return cuml_profit
