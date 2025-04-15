"""
n**2 time solution - too slow
"""
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if len(gas) == 1:
            if gas[0] - cost[0] >= 0:
                return 0
            return -1

        dist: list[int] = []

        for g, c in zip(gas, cost):
            dist.append(g-c)

        total_gas: int = sum(dist)
        if total_gas < 0:
            return -1

        # search for the biggest ramp up
        for i in range(len(dist)):
            i_prev = i - 1
            if dist[i_prev] <= 0 and dist[i] > 0:
                gas_current: int = 0
                for di in range(len(gas)):
                    k = (i + di)%len(gas)
                    gas_current += dist[k]
                    if gas_current < 0:
                        break
                else:
                    return i

        # dist: list[int] = []
        # for i in range(len(gas)):
        #     gas_current: int = 0
        #     for di in range(len(gas)):
        #         k = (i + di)%len(gas)
        #         gas_current += dist[k]
        #         if gas_current < 0:
        #             break
        #     else:
        #         return i
        # return -1
