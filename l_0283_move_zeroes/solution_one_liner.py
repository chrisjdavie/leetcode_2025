"""
Ha, so this is a cheeky one from other people's submissions. I'm not going to
say I _should_ have figured this one out, but it's an interesting use of key,
and it's a nice one-liner. But also, not clear at all why it works and slow
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=lambda x: x == 0)
