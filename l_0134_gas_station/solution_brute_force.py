"""
passes, and clear
"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        for i_start in range(len(gas)):
            tank: int = 0
            for di in range(len(gas)):
                j = (i_start + di)%len(gas)
                tank += gas[j] - cost[j]
                if tank < 0:
                    break
            else:
                return i_start
        return -1
