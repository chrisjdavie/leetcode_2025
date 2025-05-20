"""
Taken from leetcode

This, I think, reflects the best one, it incoorporates two bits of knowledge.
The first is that, each removing and adding to the list can only move the
median one position (independently), and so you can lazy-delete.

The other (that comes from the above) is that, once you have the window full,
if you add and remove from different sides, you need to shift the numbers in
stack to retain the balance between the cleaned heaps
"""
import heapq
from typing import List

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        return float("inf")
