from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        lowest: int = 10**4 + 1
        largest_profit: int = 0

        for this_price in prices:
            if this_price < lowest:
                lowest = this_price
            if (diff := this_price - lowest) > largest_profit:
                largest_profit = diff

        return largest_profit
