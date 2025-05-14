from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from heapq import heappush, heappop
from typing import List


@dataclass
class Node:

    val: int
    lower: (Node | None) = None
    higher: (Node| None) = None


class SortedSet:
    pass

class Solution:

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        return [-1]

