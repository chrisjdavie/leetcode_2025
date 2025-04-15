"""
n**2 time solution - too slow
"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        for i in range(len(gas)):
            gas_current: int = 0
            for di in range(len(gas)):
                k = (i + di)%len(gas)
                gas_current += gas[k]
                gas_current -= cost[k]
                if gas_current < 0:
                    break
            else:
                return i
        return -1
