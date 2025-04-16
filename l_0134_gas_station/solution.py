"""
passes, and clear
"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        diff: list[int] = [g - c for g, c in zip(gas, cost)]
        if sum(diff) < 0:
            return -1

        i_start_cand: int = 0
        tank: int = 0
        for i, add in enumerate(diff):
            tank += add
            if tank < 0:
                i_start_cand = i + 1
                tank = 0

        return i_start_cand
