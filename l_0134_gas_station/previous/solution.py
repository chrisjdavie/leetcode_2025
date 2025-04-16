"""
passes, and clear
"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff: list[int] = [g - c for g, c in zip(gas, cost)]
        if sum(diff) < 0:
            return -1

        # therefore, there is a _single_ answer (per problem def)
        surplus: int = 0
        i_start: int = 0

        for i, d in enumerate(diff):
            surplus += d
            if surplus < 0:
                surplus = 0
                i_start = i + 1

        return i_start
